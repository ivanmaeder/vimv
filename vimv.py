#!/usr/bin/env python

# Copyright (C) 2009, 2010 Ivan Maeder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Vi move (vimv).

A utility to help rename various files at once, using a text editor. This
script will open the list of files in a directory in a text editor (by
default, vi). Then any changes made in the editor will be reflected in the
filesystem (the files in the directory will be renamed to the names saved
in the editor). 
"""

import datetime
import logging
import os
import sys

from logging.handlers import RotatingFileHandler
from optparse import OptionParser
from tempfile import NamedTemporaryFile

__version__ = '0.2.1'

HISTORY_FILE = '~/.vimv_history'

def main():
    parser = OptionParser(usage='%prog [options] [directory ...]', version=__version__)

    #[options]
    parser.add_option('-a',
                      action='store_true',
                      default=False,
                      help='Include directory entries whose names begin with a dot.')

    parser.add_option('-e',
                      '--editor',
                      default='vi',
                      help = 'Use an alternative editor (e.g., pico).')

    parser.add_option('-v',
                      '--verbose',
                      action='store_true',
                      default=False,
                      help='Print helpful information (e.g., filename changes).')

    options, arguments = parser.parse_args()

    #[directory ...]
    dirs = arguments if arguments else [os.getcwd()]

    #initialise logger
    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.handlers.RotatingFileHandler(filename=os.path.expanduser(HISTORY_FILE), maxBytes=204800))

    #...
    for d in dirs:
        dir = os.path.realpath(d)

        try:
            #ls -a
            ls = os.listdir(dir)

            if not options.a:
                #ls
                ls = [f for f in ls if not f.startswith('.')]
        except OSError as e:
            parser.error('%s: %s' % (dir, e.strerror))

        ls.sort()

        #ls > temp_file
        with NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write('\n'.join(ls) + '\n') #\n at EOF for vi compat

        if options.verbose:
            print 'Directory "%s"' % dir

        #vi temp_file
        os.system('%s %s' % (options.editor, temp_file.name))

        #read temp_file, then delete
        try:
            with open(temp_file.name, 'rb') as f:
                file_contents = f.read().split('\n')[:-1]
        except IOError as e:
            parser.error('Unable to re-open %s: %s' % (temp_file.name, e))
        finally:
            os.remove(temp_file.name)

        #ls vs temp_file
        if len(file_contents) != len(ls):
            parser.error('Line count in file does not match directory entry count')

        #mv or rm each line in temp_file
        for i, (old_filename, new_filename) in enumerate([(a, b) for (a, b) in zip(ls, file_contents) if a != b]):
            source = dir + '/'  + old_filename

            if new_filename:
                target = os.path.abspath(os.path.join(dir, os.path.expanduser(new_filename)))
                os.system('mv "%s" "%s"' % (source, target))
            else:
                target = ''
                try:
                    os.remove(source)
                except OSError:
                    parser.error('Unable to delete: %s' % source)

            if i == 0:
                logger.debug('PID %s "%s" %s' % (os.getpid(), dir, str(datetime.datetime.now())))

            logger.debug('"%s" -> "%s"' % (source, target))

            if options.verbose:
                print 'mv %s -> %s' % (source, target)

    return 0

if __name__ == '__main__':
    sys.exit(main())
