# Vi move (vimv) - rename the files in a directory using the vi text editor

A utility to help rename various files at once, using a text editor. This script will open the list of files in a directory in a text editor (by default, vi). Then any changes made in the editor will be reflected in the filesystem (the files in the directory will be renamed to the names saved in the editor).

## Documentation
### Installation

Unix/Linux with Python:

1. Copy to `/usr/local/bin` or elsewhere on `$PATH`
2. Rename to `vimv`
3. Make executable

### Usage
On the command-line:

1. Type `vimv` to open the list of files in the current directory
2. Make the changes, save and quit

The filenames are updated when you quit. If you delete a name (leave a blank line where a filename used to be), the file will be deleted (this will not work with directories). A log of the changes is written to `~/.vimv_history`.

### Advanced

Multiple directory listings can be updated in sequence, e.g., like this:

    $vimv . ./dir1 ./dir2

Files can be moved between directories, relative names can be given in the file; double quotes should not be used in the file.

For more details run `vimv --help`.