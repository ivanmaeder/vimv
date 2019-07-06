# vimv - rename multiple files inside a text editor

`vimv` makes it easy to rename various files by letting you make the changes inside a text editor.

## How does it work?

Run `vimv` from the command-line:

```
vimv
```

This will open `vi` with the list of files in the current directory.

Change the filenames, save and exit.

The files will be renamed when you exit `vi`.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)



<iframe width="560" height="315" src="https://www.youtube.com/embed/woE6N9J6NeU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Installation

Requires Python (run `python -V` to check).

On Unix, Linux or macOS:

1. Download the script `vimv.py`
2. Copy it to `/usr/local/bin/`
3. Rename it to `vimv`
4. Make it executable (`chmod +x /usr/local/bin/vimv`)

`vimv` has NOT been tested on Windows.

You may need to run `chmod` as super user:

```
sudo chmod +x /usr/local/bin/vimv
```

## Usage
To use a different editor, e.g., the `pico` editor:

```
vimv -e pico
```

To rename ALL files in a directory, including hidden files:

```
vimv -a
```

To rename files in a different directory, e.g., in the `/home` directory:

```
vimv /home
```

To see the full list of options available:

```
vimv --help
```

### Deleting files

Delete files by leaving a blank name where a filename used to be.

### Debugging and history

A log of the changes is written to `~/.vimv_history`.

### Warning

Don't use filenames with double quotes.