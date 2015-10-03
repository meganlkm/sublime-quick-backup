# Quick File Backup

A simple ST3 plugin to backup the file you are working on.

The copied file is named `{basename}-backup-{random_numbers}.{ext}`

# Usage

Press `alt+s` and continue coding

or via the menu:

`Tools >> Packages >> QuickBackup: Backup This File`

# Configuration

To change the key binding add this, with your key binding, to your user key bindings file.

```
{ "keys": ["..."], "command": "quick_backup" }
```

# TODO

* cleanup backups
* diff
* file name template
