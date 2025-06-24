# Linux File Hierarchy Structure

The Linux File Hierarchy Structure (FHS) or Filesystem Hierarchy Standard defines the directory structure and contents in Unix-like operating systems. It is maintained by the Linux Foundation.

## / (Root):

- Primary hierarchy root and root directory of the entire file system hierarchy.
- Every single file and directory starts from the root directory.
- Only the root user has the right to write under this directory.
- `/root` is the root user’s home directory, which is not the same as `/`.

![1](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/31253e47-fc9a-48b9-b7cd-a3dd95297371)


## /bin:

- Essential command binaries that need to be available in single-user mode and for all users.
- Contains binary executables for common Linux commands used in single-user modes and by all users of the system.

![2](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/9b12a786-158b-4d12-be66-5543b8cbba33)


## /boot:

- Boot loader files, such as kernels and initrd.

![3](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/ce77ae20-fceb-4ab8-b6af-f39629469b9c)


## /dev:

- Essential device files, such as `/dev/null`, terminal devices, and USB devices.

![4](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/5cd54d10-57c0-47ff-9411-ee45a8356560)


## /etc:

- Host-specific system-wide configuration files, including startup and shutdown scripts.
- Contains configuration files required by all programs.

![8](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/79ba7510-3943-45f8-ae0a-ba1fb57bb157)


## /home:

- Users’ home directories, containing saved files and personal settings.

![5](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/f354e11d-0cf3-43fb-bed7-d6cf7be1aa87)


## /lib:

- Libraries essential for binaries in `/bin` and `/sbin`.

![6](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/e294c575-54c6-4329-922e-49b2a5e0e510)


## /media:

- Mount points for removable media such as CD-ROMs.

![7](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/972446a0-92f3-4bb5-99ba-f5007676fd2a)


## /mnt:

- Temporarily mounted filesystems.

![9](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/934062bb-65c2-4a21-a3aa-ac8dce48f5e7)

## /opt:

- Optional application software packages.

![10](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/14d07205-6314-451b-8204-54e364e35a0b)

## /sbin:

- Essential system binaries used by system administrators for maintenance purposes.

![11](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/1d4de7bd-6bb4-4c2f-ad2f-4be8564d7927)


## /srv:

- Site-specific data served by the system, such as data for web servers and version control systems.

![12](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/e24bc9fb-3a6e-4305-b831-933f9f0c7cda)


## /tmp:

- Temporary files that are not preserved between system reboots.

![13](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/44c6c060-9635-4bef-b636-1d2a34231f7e)


## /usr:

- Secondary hierarchy for read-only user data and contains utilities and applications for users.
- `/usr/bin` contains binary files for user programs, and `/usr/sbin` contains binaries for system administrators.
- Libraries, documentation, and source code are also found in `/usr`.

![14](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/c8a11c8b-06ab-4ae3-8f69-901a1b2b038c)


## /proc:

- Virtual filesystem providing process and kernel information as files.
- Contains information about running processes and system resources.

![15](https://github.com/MaheshShukla1/Linux-Basic-to-Advanced-Notes/assets/95337825/2cdcdc96-4405-413b-acc1-aa3f41015673)


Modern Linux distributions include a `/run` directory as a temporary filesystem (tmpfs) which stores volatile runtime data, following the FHS version 3.0.

## Conclusion

Understanding the Linux File Hierarchy Structure is crucial for navigating and managing Unix-like operating systems effectively. By familiarizing yourself with the key directories and their purposes, you gain insights into how the system is organized and where to find essential files and configurations. Whether you're a system administrator, developer, or Linux enthusiast, mastering the FHS enhances your ability to work efficiently within the Linux environment.

Happy exploring and navigating the Linux filesystem!

---

*References:*

1. [Filesystem Hierarchy Standard (FHS)](https://refspecs.linuxfoundation.org/fhs.shtml)
2. [Linux Filesystem Hierarchy](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
3. [Understanding the Linux Directory Structure](https://opensource.com/article/19/2/linux-directory-structure)
4. [Linux Documentation](https://www.kernel.org/doc/html/latest/)


