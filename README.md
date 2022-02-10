## Description
This script automate the instructions in the [oficial website](https://github.com/osxfuse/osxfuse/wiki/NTFS-3G) to remount the partition in read and write mode

## Install ntfs-3g
```bash
brew tap gromgit/homebrew-fuse
brew install ntfs-3g-mac
```
## Enable security extensions
This is a good tutorial about this procedure: https://iboysoft.com/howto/enable-system-extension-m1-mac.html

## Install this utility
We recommend to [install pipx](https://github.com/pypa/pipx#install-pipx) first and run this command
```bash
pipx install git+https://github.com/rodfersou/osx-ntfs-rw.git
```

## Plug the device and trigger the utility 

```bash
sudo ntfs-rw
```
