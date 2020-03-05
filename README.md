# Override 'rm' in linux

### This repo aims at overriding 'rm' instruction in linux to prevent you from some harmful commands.<br>Instead of deleting files forever, the overrided 'rm' moves files into a trashbin where you can restore files.

#### Prerequisite

* Python3

### Install

1. Build executable file

   ```bash
   pip install pyinstaller
   pyinstaller /path/to/this/repo/rm.py
   ```

2. Build Trashbin in a large disk, and link it to your home directory.

   ```bash
   mkdir TrashBin
   ln -s /path/to/TrashBin ~/
   ```

3. Append following lines to your .bashrc or .zshrc

   ```bash
   alias rm='/path/to/this/repo/dist/rm/rm'
   alias rmf='/bin/rm'
   ```

   **remember to re-login or 'source .bashrc(.zshrc)' to activate the aliases.**

### Usage

1. 'Delete' file

   ```bash
   rm file/to/delte
   ```

2. 'Delete' directory

   ```bash
   rm directory/to/delete
   ```

3. Find 'deleted' file or directory

   ```bash
   cd ~/TrashBin # goto trashbin
   cat .rm-log.txt # view delete log
   # select what you need, and move it to where you want by 'mv'
   ```

### Notes

1. This script add suffix for identical file names, for example, doin 'rm 1.txt' twice will generates '1.txt' and '1.txt.1' in trashbin. Differ them by viewing delete log '~/TrashBin/.rm-log.txt'
2. This script **does not** empty your trashbin automatically, so you need to clear your trashbin manually by 'rmf'.

