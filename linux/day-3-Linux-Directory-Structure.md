# Linux Directory Structure
 
**Prerequisite:** Linux File Hierarchy Structure

## Introduction

In Linux and Unix operating systems, everything is considered a file, including directories, regular files, and devices like mouse, keyboard, and printers. This document provides an in-depth overview of the Linux directory structure, including types of files and the hierarchy of directories.

## Types of Files in Linux
#### General Files
* General files, also known as ordinary files, can be of various types, such as images, videos, programs, or simple text files. These files can be in ASCII or Binary format and are the most commonly used files in the Linux system.

#### Directory Files
* Directory files act as a warehouse for other file types. They organize files and may include subdirectories within them, creating a hierarchical structure for file management.

#### Device Files
* Unlike Windows-like operating systems where devices are represented as drive letters, Linux represents devices as files. For example, /dev/sda1, /dev/sda2 represent different partitions of a hard drive.

## Types of Files in Linux

| **File Types**   | **Description**                                                                                         |
|------------------|---------------------------------------------------------------------------------------------------------|
| General Files    | Also known as ordinary files, they can be images, videos, programs, or simple text files.              |
| Directory Files  | Act as a warehouse for other file types, organizing files and including subdirectories.                 |
| Device Files     | Represent devices as files, such as /dev/sda1 for partitions of a hard drive.                           |

## Linux File System Hierarchy

The Linux file system hierarchy begins with the root directory /. Here are some of the top-level directories and their purposes:

| **Directory**    | **Description**                                                |
|------------------|----------------------------------------------------------------|
| /bin             | Contains binary or executable programs.                         |
| /etc             | Stores system configuration files.                              |
| /home            | Default home directory for users.                               |
| /opt             | Location for optional or third-party software.                  |
| /tmp             | Temporary space, usually cleared on system reboot.              |
| /usr             | Contains user-related programs.                                 |
| /var             | Holds log files and variable data.                              |
| **Additional Directories** |
| /boot            | Boot-related information.                                      |
| /dev             | Device files location.                                         |
| /lib             | Kernel modules and shared libraries.                            |
| /lost+found      | Used for recovered bits of corrupted files.                     |
| /media           | Subdirectories for removable media devices.                     |
| /mnt             | Temporary mount directories.                                    |
| /proc            | Virtual file system containing process information.             |
| /run             | Stores volatile runtime data.                                   |
| /sbin            | System binaries for administrators.                             |
| /srv             | Server-specific files.                                          |
| /sys             | Virtual file system for device information.                     |

## Notable Files in Linux

| **File/Directory** | **Description**                                                |
|--------------------|----------------------------------------------------------------|
| Linux Kernel File  | /boot/vmlinux: The Linux kernel file.                           |
| Device Files       | /dev/hda: Device file for the first IDE HDD.                    |
|                    | /dev/hdc: Pseudo-device for garbage output redirection.         |
| System Config Files| /etc/bashrc: Bash shell system defaults and aliases.            |
|                    | /etc/crontab: Shell script for scheduled commands.              |
|                    | /etc/fstab: Disk drive information and mount points.            |
|                    | /etc/group: Information about security groups.                  |
|                    | /etc/grub.conf: Grub bootloader configuration.                  |
|                    | /etc/init.d: Scripts for service startup.                       |
|                    | /etc/inittab: Initialization process and run levels.            |
|                    | /etc/passwd: Usernames and passwords.                           |
|                    | /etc/resolv.conf: DNS configuration.                            |
| User Files         | /usr/bin: Executable files.                                     |
|                    | /usr/include: Standard files for C programs.                     |
|                    | /usr/lib: Object files and libraries.                            |
| Virtual Files      | /proc/cpuinfo: CPU information.                                  |
|                    | /proc/filesystems: Information about running processes.          |
|                    | /proc/ioports: Input and Output addresses used by devices.       |
|                    | /proc/meminfo: Memory usage information.                         |
| Other Important Files | Version Information File: /version - Displays Linux version information. |
|                    | Log Files:                                                     |
|                    | /var/log/lastlog: User's last login information.                |
|                    | /var/log/messages: Global system messages.                       |
|                    | /var/log/wtmp: Login and logout history.                         |

## Conclusion

Understanding the Linux directory structure is essential for efficient system navigation, file management, and access to system resources. While variations may exist across different Linux distributions, the fundamental organization remains consistent.

For detailed explanations and examples, refer to the [Linux Directory Structure wiki page](https://github.com/MaheshShukla1/Linux-Directory-Structure/wiki/Linux-Directory-Structure).
