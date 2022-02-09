# https://github.com/osxfuse/osxfuse/wiki/NTFS-3G 
brew tap gromgit/homebrew-fuse
brew install ntfs-3g-mac
# enable security extensions
# sudo diskutil list
# sudo diskutil umount disk6s1
# sudo ntfs-3g /dev/disk6s1 /Volumes/NTFS -o local -o allow_other -o auto_xattr -o auto_cache
