import sys
from collections import namedtuple
from subprocess import PIPE, Popen

from pick import pick

Disk = namedtuple("Disk", ["type", "name", "size", "identifier"])


def select_disk() -> Disk:
    command = "diskutil list"
    result = Popen(command, shell=True, stdout=PIPE).stdout.readlines()
    # Remove unicode chars
    result = [r.decode().encode("ascii", "ignore").decode() for r in result]
    # Clean line break
    result = [r.rstrip("\n") for r in result]
    # Break in list of items
    result = [r.split() for r in result]
    # Remove empty lines
    result = [r for r in result if r]
    # Filter out group titles
    result = [r for r in result if len(r) >= 5]
    # Filter out titles
    result = [r for r in result if r[0] != "#:"]
    # Remove index column
    result = [r[1:] for r in result]
    # Fix structure
    invalid_names = ["Container", "Volume", "Snapshot"]
    result = [
        [
            r[0],
            r[1] if len(r) > 4 and r[1] not in invalid_names else "",
            f"{r[-3]} {r[-2]}",
            r[-1],
        ]
        for r in result
    ]

    # Instantiate object
    disks = [Disk(*r) for r in result]

    # Select partition
    disks = [disk for disk in disks if disk.type == "Windows_NTFS"]
    if len(disks) == 1:
        selected = disks[0]
    else:
        selected, _ = pick(disks)

    return selected


def main():
    disk = select_disk()
    # Umount partition
    command = f"diskutil umount {disk.identifier}"
    Popen(command, shell=True)
    # Create folder
    command = f"mkdir /Volumes/{disk.name}"
    Popen(command, shell=True)
    # Mount partition
    command = f"ntfs-3g /dev/{disk.identifier} /Volumes/{disk.name} -o local -o allow_other -o auto_xattr -o auto_cache"
    Popen(command, shell=True)


if __name__ == "__main__":
    sys.exit(main())
