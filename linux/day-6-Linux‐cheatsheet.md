# Essential Commands

We recommend that you memorize these commands. You’ll need them the most when operating Linux.

## File Management

In the following commands: `X` may refer to a single file, a string containing a wildcard symbol referring to a set of multiple files, e.g., `file*.txt`, or the stream output of a piped command (in which case the syntax would be `X | command` instead of `command X`); `Y` is a single directory; `A` and `B` are path strings of files/directories.

| COMMAND               | DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `*`                   | Wildcard symbol for variable length, e.g., `*.txt` refers to all files with the TXT extension                                                                                                                                                                                                                                                                                  |
| `?`                   | Wildcard symbol referring to a single character, e.g., `Doc?.docx` can refer to `Doc1.docx`, `DocA.docx`, etc.                                                                                                                                                                                                                                                                 |
| `ls`                  | List the names of files and subfolders in the current directory. Options include `-l, -a, -t` which you may combine, e.g., `-alt`.                                                                                                                                                                                                                                             |
| `ls -l`               | Also show details of each item displayed, such as user permissions and the time/date when the item was last modified                                                                                                                                                                                                                                                           |
| `ls -a`               | Also display hidden files/folders. May be combined with `ls -l` to form `ls -al`.                                                                                                                                                                                                                                                                                              |
| `ls -t`               | Sort the files/folders according to the last modified time/date, starting with the most recently modified item                                                                                                                                                                                                                                                                 |
| `ls X`                | List the files                                                                                                                                                                                                                                                                                                                                                                 |
| `cd Y`                | Change directory to `Y`.  <br>  <br>Special instances of `Y`:  <br>`.`  — current directory  <br>`..` — parent directory                                                                                                                                                                                                                                                       |
| `cd`                  | To the `$HOME` directory                                                                                                                                                                                                                                                                                                                                                       |
| `cd ..`               | Up one level to enclosing folder or parent directory                                                                                                                                                                                                                                                                                                                           |
| `cd /etc`             | To the `/etc` directory                                                                                                                                                                                                                                                                                                                                                        |
| `cmp A B`             | Compare two files `A` and `B` for sameness. No output if `A` and `B` are identical, outputs character and line number otherwise.                                                                                                                                                                                                                                               |
| `diff A B`            | Compare two files `A` and `B` for differences. Outputs the difference.                                                                                                                                                                                                                                                                                                         |
| `pwd`                 | Display the path of the current working directory.                                                                                                                                                                                                                                                                                                                             |
| `mkdir X`             | Make a new directory named `X` inside the current directory.                                                                                                                                                                                                                                                                                                                   |
| `mv A B`              | Move a file from path `A` to path `B`. Also used for renaming files.  <br>Examples:  <br>- Moving between directories `folder1` and `folder2`:  <br>`mv ./folder1/file.txt ./folder2`  <br>The file name will remain unchanged, and its new path will be `./folder2/file.txt`.  <br>- Renaming a file: `mv new_doc.txt expenses.txt`  <br>The new file name is `expenses.txt`. |
| `cp A B`              | Copy a file from path `A` to path `B`. Usage similar to `mv` both in moving to a new directory and simultaneously renaming the file in its new location.  <br>Example: `cp ./f1/file.txt ./f2/expenses.txt` simultaneously copies the file `file.txt` to the new location with a new name `expenses.txt`.                                                                      |
| `cp -r Y Z`           | Recursively copy a directory `Y` and its contents to `Z`. If `Z` exists, copy source `Y` into it; otherwise, create `Z` and `Y` becomes its subdirectory with `Y`’s contents                                                                                                                                                                                                   |
| `rm X`                | Remove (delete) `X` permanently.                                                                                                                                                                                                                                                                                                                                               |
| `rm -r Y`             | Recursively delete a directory `Y` and its contents                                                                                                                                                                                                                                                                                                                            |
| `rm -f X`             | Forcibly remove file `` `X` `` without prompts or confirmation                                                                                                                                                                                                                                                                                                                 |
| `rm -rf Y`            | Forcibly remove directory `Y` and its contents recursively                                                                                                                                                                                                                                                                                                                     |
| `rmdir Y`             | Remove a directory `Y` permanently, provided `Y` is empty.                                                                                                                                                                                                                                                                                                                     |
| `open X`              | Open `X` in its default program.                                                                                                                                                                                                                                                                                                                                               |
| `open -e X`           | Opens `X` in the default text editor (macOS: TextEdit)                                                                                                                                                                                                                                                                                                                         |
| `touch X`             | Create an empty file `X` or update the access and modification times of `X`.                                                                                                                                                                                                                                                                                                   |
| `cat X`               | View contents of `X`.                                                                                                                                                                                                                                                                                                                                                          |
| `cat -b X`            | Also display line numbers as well.                                                                                                                                                                                                                                                                                                                                             |
| `wc X`                | Display word count of `X`.                                                                                                                                                                                                                                                                                                                                                     |
| `head X`              | Display the first 10 lines of `X`. If more than a single file is specified, each file is preceded by a header consisting of the string "`==> X <==`'' where "`X`'' is the name of the file.                                                                                                                                                                                    |
| `head -n 4 X`         | Show the first 4 lines of `X`.                                                                                                                                                                                                                                                                                                                                                 |
| `ls *.c \| head -n 5` | Display the first 5 items of a list of `*.c` files in the current directory.                                                                                                                                                                                                                                                                                                   |
| `tail X`              | Display the last (10, by default) lines of `X`. If more than a single file is specified, each file is preceded by a header consisting of the string "`==> X <==`'' where "`X`'' is the name of the file.                                                                                                                                                                       |
| `tail -n +1 X`        | Display entire contents of the file(s) `X` specified, with header of respective file names                                                                                                                                                                                                                                                                                     |
| `tail -f X`           | Display the last 10 lines of the file(s) `X` specified, and track changes appended to them at the end. Overwriting `X` or modifying `X` with a text editor such as vim would mess up this command’s output.                                                                                                                                                                    |
| `less`                | Read a file with forward and backward navigation. Often used with pipe, e.g., `cat file.txt \| less`                                                                                                                                                                                                                                                                           |
| `ln -s A S`           | Create symbolic link of path `A` to link name `S`.                                                                                                                                                                                                                                                                                                                             |

### Input/Output Redirection

These are helpful for logging program output and error messages.

|COMMAND|DESCRIPTION|
|---|---|
|`echo TEXT`|Display a line of `TEXT` or the contents of a variable.|
|`echo -e TEXT`|Also interprets escape characters in `TEXT`, e.g., `\n →` new line, `\b →` backslash, `\t →` tab.|
|`echo -n TEXT`|Omits trailing newline of `TEXT`.|
|`cmd1 \| cmd2`|`\|` is the pipe character; feeds the output of the command `cmd1` and sends it to the command `cmd2`, e.g., `ps aux \| grep python3`.|
|`cmd > file`|Redirect output of a command `cmd` to a file `file`. Overwrites pre-existing content of `file`.|
|`cmd >& file`|Redirect output of `cmd` to `file`. Overwrites pre-existing content of `file`. Suppresses the output of `cmd`.|
|`cmd > /dev/null`|Suppress the output of `cmd`.|
|`cmd >> file`|Append output of `cmd` to `file`.|
|`cmd < file`|Read input of `cmd` from `file`.|
|`cmd << delim`|Read input of `cmd` from the standard input with the delimiter character `delim` to tell the system where to terminate the input. Example for counting the number of lines of ad-hoc input:  <br>`wc -l << EOF`  <br>`> I like   > apples   > and   > oranges.   > EOF`        <br> `4`  <br>Hence there are only 4 lines in the standard input delimited by `EOF`.|
|`cmd <<< string`|Input a text `string` to `cmd`.|
|`cmd 2> foo`|Redirect error messages of `cmd` to `foo`.|
|`cmd 2>> foo`|Append error messages of `cmd` to `foo`.|
|`cmd &> file`|Redirect output and error messages of `cmd` to `file`.|

### Search and Filter

These commands help you find the files you want.

|COMMAND|DESCRIPTION|
|---|---|
|`grep patt /path/to/src`|Search for a text pattern `patt` in `X`. Commonly used with pipe e.g., `ps aux \| grep python3` filters out the processes containing `python3` from all running processes of all users.|
|`grep -r patt /path/to/src`|Search recursively (the target directory `/path/to/src` and its subdirectories) for a text pattern `patt`.|
|`grep -v patt X`|Return lines in `X` not matching the specified `patt`.|
|`grep -l patt X`|Write to standard output the names of files containing `patt`.|
|`grep -i patt X`|Perform case-insensitive matching on `X`. Ignore the case of `patt`.|
|`find`|Find files.|
|`find /path/to/src -name "*.sh"`|Find all files in `/path/to/src` matching the pattern "`*.sh`" in the file name.|
|`find /home -size +100M`|Find all files in the `/home` directory larger than 100MB.|
|`locate name`|Find files and directories by `name`.|
|`sort X`|Arrange lines of text in `X` alphabetically or numerically.|

### Archives

These commands are for unpacking compressed files (`.zip, .gz, .bz2, .tar,` etc.) with large or complex contents, such as programs.

|COMMAND|DESCRIPTION|
|---|---|
|`tar`|Manipulate archives with `.tar` extension.|
|`tar -v`|Get verbose output while manipulating TAR archives. May combine this option with others, e.g., `tar -tvf`.|
|`tar -cf archive.tar Y`|Create a TAR archive named `archive.tar` containing `Y`.|
|`tar -xf archive.tar`|Extract the TAR archive named `archive.tar`.|
|`tar -tf archive.tar`|List contents of the TAR archive named `archive.tar`.|
|`tar -czf archive.tar.gz Y`|Create a gzip-compressed TAR archive named `archive.tar.gz` containing `Y`.|
|`tar -xzf archive.tar.gz`|Extract the gzip-compressed TAR archive named `archive.tar.gz`.|
|`tar -cjf archiave.tar.bz2 Y`|Create a bzip2-compressed TAR archive named `archive.tar.bz2` containing `Y`.|
|`tar -xjf archive.tar.bz2`|Extract the bzip2-compressed TAR archive named `archive.tar.bz2`.|
|`gzip`|Manipulate archives with `.gz` extension.|
|`gzip Y`|Create a gzip archive named `Y.gz` containing `Y`.|
|`gzip -l Y.gz`|List contents of gzip archive `Y.gz`.|
|`gzip -d Y.gz`  <br>`gunzip Y.gz`|Extract `Y.gz` and recover the original file `Y`.|
|`bzip2`|Manipulate archives with `.bz2` extension.|
|`bzip2 Y`|Create a bzip2 archive named `Y.bz2` containing `Y`.|
|`bzip2 -d Y.gz`  <br>`bunzip2 Y.gz`|Extract `Y.bz2` and recover the original file `Y`.|
|`zip -r Z.zip Y`|Zip `Y` to the ZIP archive `Z.zip`.|
|`unzip Z.zip`|Unzip `Z.zip` to the current directory.|
|`unzip Z.zip`|List contents of `Z.zip`.|

## File Transfer

These commands are for logging in to local and remote hosts, and for uploading and downloading files, transferring them between devices. Remember to omit the square brackets "`[`" and "`]`" when you input the optional parameters they enclose.

|COMMAND|DESCRIPTION|
|---|---|
|`ssh user@access`|Connect to `access` as `user`.|
|`ssh access`|Connect to `access` as your local username.|
|`ssh -p port user@access`|Connect to `access` as `user` using `port`.|
|`scp [user1@]host1:[path1] [user2@]host2:[path2]`|Login to `hostN` as `userN` via secure copy protocol for `N=1,2`.  <br>  <br>Example usage:  <br>`scp alice@pi:/home/source bob@arduino:/destination`  <br>  <br>`path1` and `path2` may be local or remote, but ensure they’re absolute rather than relative paths, e.g., `/var/www/*.html`, `/usr/bin`.  <br>  <br>If `user1` and `user2` are not specified, `scp` will use your local username.|
|`scp -P port [user1@]host1:[path1] [user2@]host2:[path2]`|Connect to `hostN` as `userN` using port for `N=1,2`.|
|`scp -r [user1@]host1:[path1] [user2@]host2:[path2]`|Recursively copy all files and directories from `path1` to `path2`.|
|`sftp [user@]access`|Login to `access` as `user` via secure file transfer protocol. If `user` is not specified, your local username will be used.|
|`sftp access`|Connect to `access` as your local username.|
|`sftp -P port user@access`|Connect to `access` as `user` using `port`.|
|`rsync -a [path1] [path2]`|Synchronize `[path1]` to `[path2]`, preserving symbolic links, attributes, permissions, ownerships, and other settings.|
|`rsync -avz host1:[path1] [path2]`|Synchronize `[path1]` on the remote host `host1` to the local path `[path2]`, preserving symbolic links, attributes, permissions, ownerships, and other settings. It also compresses the data involved during the transfer.|

## File Permissions
Not all files are equally accessible. To prevent unwanted tampering, some files on your device may be read-only. For more information about file permissions on Linux, refer to our [Linux File Permissions Cheat Sheet](https://www.stationx.net/linux-file-permissions-cheat-sheet/).
![Linux file type - regular file, d directory, l symbolic link; scope u user, g group, o other, a all; permissions r read, w write, x execute](https://www.stationx.net/wp-content/uploads/2022/12/Linux-file-type-regular-file-d-directory-l-symbolic-link-scope-u-user-g-group-o-other-a-all-permissions-r-read-w-write-x-execute.png "Linux: file type: - regular file, d directory, l symbolic link; scope: u user, g group, o other, a all; permissions: r read, w write, x execute")

|COMMAND|DESCRIPTION|
|---|---|
|`chmod permission file`|Change permissions of a file or directory. Permissions may be of the form `[u/g/o/a][+/-/=][r/w/x]` (see examples below) or a three-digit octal number.|
|`chown user2 file`|Change the owner of a file to `user2`.|
|`chgrp group2 file`|Change the group of a file to `group2`.|

Usage examples:

- `chmod +x testfile` → allow all users to execute the file
- `chmod u-w testfile` → forbid the current user from writing or changing the file
- `chmod u+wx,g-x,o=rx testfile` → simultaneously add write and execute permissions to user, remove execute permission from group, and set the permissions of other users to only read and write.

### Numeric Representation

The table below compares Linux file permissions in octal form and in the format `[u/g/o/a][+/-/=][r/w/x]`.

| OCTAL | PERMISSION(S)                                 | EQUIVALENT TO APPLICATION OF |
| ----- | --------------------------------------------- | ---------------------------- |
| `0`   | No permissions                                | `-rwx`                       |
| `1`   | Execute permission only                       | `=x`                         |
| `2`   | Write permission only                         | `=w`                         |
| `3`   | Write and execute permissions only: 2 + 1 = 3 | `=wx`                        |
| `4`   | Read permission only                          | `=r`                         |
| `5`   | Read and execute permissions only: 4 + 1 = 5  | `=rx`                        |
| `6`   | Read and write permissions only: 4 + 2 = 6    | `=rw`                        |
| `7`   | All permissions: 4 + 2 + 1 = 7                | `=rwx`                       |

### Examples

- `chmod 777 testfile` → allow all users to execute the file
- `chmod 177 testfile` → restrict current user (`u`) to execute-only, while the group (`g`) and other users (`o`) have read, write and execute permissions
- `chmod 365 testfile` → user (`u`) gets to write and execute only; group (`g`), read and write only; others (`o`), read and execute only.

### Other Links You Might Like:

- [Linux File Permissions Cheat Sheet](https://www.stationx.net/linux-file-permissions-cheat-sheet/)
- [Unix Commands Cheat Sheet](https://www.stationx.net/unix-commands-cheat-sheet/)
- [Tmux Cheat Sheet](https://www.stationx.net/tmux-cheat-sheet/)
- [Tcpdump Cheat Sheet](https://www.stationx.net/tcpdump-cheat-sheet/)
- [Bash Cheat Sheet](https://www.stationx.net/bash-cheat-sheet/)
- [Vi Cheat Sheet](https://www.stationx.net/vi-cheat-sheet/)
- [Our Linux Courses Collection](https://courses.stationx.net/courses?query=linux)

## System Information

These commands come in handy when you’re developing new applications for Linux or troubleshooting your Linux machine.

### General

These provide information about your Linux machine and perform administrative tasks.

|COMMAND|DESCRIPTION|
|---|---|
|`uname`|Show the Linux system information.|
|`uname -a`|Detailed Linux system information|
|`uname -r`|Kernel release information, such as kernel version|
|`uptime`|Show how long the system is running and load information.|
|`su`  <br>`sudo`|Superuser; use this before a command that requires root access e.g., `su shutdown`|
|`cal`|Show calendar where the current date is highlighted.|
|`date`|Show the current date and time of the machine.|
|`halt`|Stop the system immediately.|
|`shutdown`|Shut down the system.|
|`reboot`|Restart the system.|
|`last reboot`|Show reboot history.|
|`man COMMAND`|Shows the manual for a given `COMMAND`. To exit the manual, press “q”.|
|`hostname`|Show system host name|
|`hostname -I`|Display IP address of host|
|`cat /etc/*-release`|Show the version of the Linux distribution installed. For example, if you’re using Red Hat Linux, you may replace * with `redhat`.|

### Hardware

These commands provide details about the hardware supporting your Linux machine.

|COMMAND|DESCRIPTION|
|---|---|
|`dmesg`|Display messages in kernel ring buffer (data structure that records messages related to the operation of the program running the operating system)|
|`cat /proc/cpuinfo`|Display information about the central processing unit (CPU)|
|`cat /proc/meminfo`|Display memory information|
|`lspci -tv`|Displays information about each Peripheral Component Interconnect (PCI) device on your system.  <br>The option `-t` outputs the information as a tree diagram, and `-v` is for verbose output.|
|`lsusb -tv`|Display information about Universal Serial Bus (USB) devices and the devices connected to them.  <br>The option `-t` outputs the information as a tree diagram, and `-v` is for verbose output.|
|`dmidecode`|Display system hardware components, serial numbers, and BIOS version|
|`hdparm -i /dev/sda`|Display information about the disk `sda`|
|`hdparm -tT /dev/sda`|Perform a read speed test on the disk `sda`|
|`badblocks -s /dev/sda`|Test for unreadable blocks on the disk `sda`|

### Disk Usage

These commands provide storage details regarding your Linux machine.

|COMMAND|DESCRIPTION|
|---|---|
|`df`|Display free disk space.|
|`du`|Show file/folder sizes on disk.|
|`du -ah`|Disk usage in human readable format (KB, MB etc.)|
|`du -sh`|Total disk usage of the current directory|
|`du -h`|Free and used space on mounted filesystems|
|`du -i`|Free and used inodes on mounted filesystems|
|`fdisk -l`|List disk partitions, sizes, and types|
|`free -h`|Display free and used memory in human readable units.|
|`free -m`|Display free and used memory in MB.|
|`free -g`|Display free and used memory in GB.|

## Process Management and Performance Monitoring

The following is redolent of functions in Windows Task Manager, but on the command line.

|COMMAND|DESCRIPTION|
|---|---|
|`&`|Add this character to the end of a command/process to run it in the background|
|`ps`|Show process status. Often used with `grep` e.g., `ps aux \| grep python3` displays information on processes involving `python3`.  <br>  <br>Meaning of `aux`:  <br>`a` = show processes for all users  <br>`u` = show user or owner column in output  <br>`x` = show processes not attached to a terminal|
|`ps -e`  <br>`ps -A`|Either of these two commands prints all running processes in the system|
|`ps -ef`|Print detailed overview|
|`ps -U root -u root`|Display all processes running under the account `root`.|
|`ps -eo pid,user,command`|Display only the columns `pid`, `user` and `command` in `ps` output|
|`top`|Display sorted information about processes|
|`htop`|Display sorted information about processes with visual highlights. It allows you to scroll vertically and horizontally, so you can see every process running on your system and entire commands.|
|`atop`|Display detailed information about processes and hardware|
|`kill PID`|Kill a process specified by its process ID `PID`, which you obtain using the `ps` command|
|`killall proc1`|Kill all processes containing `proc1` in their names|
|`lsof`|List all open files on the system. (This command helps you pinpoint what files and processes are preventing you from successfully ejecting an external drive.)|
|`lsof -u root`|List all files on the system opened by the `root` user. As the output can be long, you may use `lsof -u root \| less` to keep this list from taking up space in the terminal output.|
|`mpstat 1`|Display processor-related statistics, updated every second (hence the `1`, whereas `mpstat 2` refreshes the output every 2 seconds)|
|`vmstat 1`|Display virtual memory statistics (information about memory, system processes, paging, interrupts, block I/O, disk, and CPU scheduling), updated every (`1`) second|
|`iostat 1`|Display system input/output statistics for devices and partitions. virtual memory statistics, updated every (`1`) second|
|`tail -n 100 /var/log/messages`|Display the last 100 lines in the system logs.  <br>Replace `/var/log/messages` with `/var/log/syslog` for Debian-based systems.|
|`tcpdump -i eth0`|Capture and display all packets on interface `eth0`|
|`tcpdump -i eth0 port 80`|Monitor all traffic on interface `eth0` port 80 (HTTP)|
|`watch df -h`|Execute `df -h` and show periodic updates.  <br>To exit, press **Ctrl+C**.|

## User Management

These commands give information on the system’s users and allows superuser administrators to change user settings.

|COMMAND|DESCRIPTION|
|---|---|
|`who`|Display who is logged in|
|`w`|Display what users are online and what they are doing|
|`users`|List current users|
|`whoami`|Display what user you are logged in as|
|`id`|Display the user ID and group IDs of your current user|
|`last`|Display the last users who have logged onto the system|
|`groupadd gp1`|Create a group named `gp1`|
|`useradd -c "Alice Bob" -m ab1`|Create an account named `ab1`, with a comment of "`Alice Bob`" and create the new user’s home directory|
|`userdel ab1`|Delete the account named `ab1`|
|`usermod -aG gp1 ab1`|Add the account `ab1` to the group `gp1`|

## Networking

These commands regulate how your Linux machine communicates with other computers, such as the local area network (LAN) router or external websites.

| COMMAND          | DESCRIPTION                                                                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ifconfig`       | Display all network interfaces with IP addresses                                                                                                                                                  |
| `ifconfig -a`    | Display all network interfaces, even if any of them is down, with IP addresses                                                                                                                    |
| `ifconfig eth0`  | Display IP addresses and details of the `eth0` interface                                                                                                                                          |
| `ip a`           | Another way to display all network interfaces with IP addresses                                                                                                                                   |
| `ethtool eth0`   | Query or control network driver and hardware settings of the interface `eth0`                                                                                                                     |
| `netstat`        | Print open sockets of network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.  <br>Pipe with the `less` command: e.g., `netstat -a \| less` |
| `netstat -a`     | Show both listening and non-listening sockets                                                                                                                                                     |
| `netstat -l`     | Show only listening sockets                                                                                                                                                                       |
| `netstat -nutlp` | Show listening TCP and UDP ports and corresponding programs                                                                                                                                       |
| `ping host`      | Send ICMP echo request to `host`, which may be a symbolic name, domain name or IP address                                                                                                         |
| `whois domain`   | Display whois information for `domain`                                                                                                                                                            |
| `dig domain`     | Display DNS information for `domain`                                                                                                                                                              |
| `dig -x addr`    | Do a reverse lookup on an IPv4 or IPv6 address `addr`                                                                                                                                             |
| `host domain`    | Display DNS IP address for `domain`                                                                                                                                                               |
| `wget LINK`      | Download from location `LINK`                                                                                                                                                                     |
| `curl LINK`      | Display the HTML source of `LINK`. Check out our [curl Cheat Sheet](https://www.stationx.net/curl-cheat-sheet/) for details.                                                                      |

## Installing New Programs

A package file is an archive containing compiled software and other resources it uses. The package file extension and the package installer (a utility for installing new programs) depend on the Linux distribution.

Know your system’s Linux distribution to understand the correct installation commands tailored to it. If the package comes with a README component, it should contain application-specific installation instructions such as extracting TAR files (refer to this article’s [Archives](https://www.stationx.net/linux-command-line-cheat-sheet/#archives) section), `./setup.sh`, and `make install`.

### Package Management Overview

The following table is on package management in popular Linux distributions.

|LINUX DISTRIBUTION|PACKAGE FILE EXTENSION|PACKAGE INSTALLER(S)|
|---|---|---|
|Debian / Ubuntu|`.deb`|`apt, dpkg`|
|Rocky / Fedora / Red Hat Enterprise Linux|`.rpm`|`yum, dnf`|
|Arch Linux / Manjaro / Garuda / Chakra|`.pkg, .pacman, .pkg.tar(.xz/.zst/.gz)`|`pacman`|

### Package Management Commands

Here are the commands for package management in popular Linux distributions.

| LINUX DISTRIBUTION                                                           | DEBIAN / UBUNTU            | ROCKY / FEDORA / RED HAT ENTERPRISE LINUX | ARCH LINUX / MANJARO / GARUDA / CHAKRA                                                                      |
| ---------------------------------------------------------------------------- | -------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Update list of packages available from remote repositories                   | `sudo apt update`          | `dnf check-update`                        | The command `pacman -Syy` achieves this purpose but may damage your system.  <br>Use `pacman -Syu` instead. |
| Upgrade installed packages                                                   | `sudo apt upgrade`         | `sudo dnf upgrade`                        | `pacman -Syu`                                                                                               |
| Find a package with keyword in the name                                      | `apt search keyword`       | `dnf search keyword`                      | `pacman -Ss keyword`                                                                                        |
| View description and summary information about a package                     | `apt show package`         | `dnf info package`                        | `pacman -Si package`                                                                                        |
| Install a package (with appropriate file extension) on the local file system | `sudo dpkg -i package.deb` | `sudo dnf install package.rpm`            | `pacman -S package`                                                                                         |
| Remove / uninstall a package                                                 | `sudo apt remove package`  | `sudo dnf erase package`                  | 
`pacman -R package`                                                                                         |

![logos](https://github.com/MaheshShukla1/Linux-Fundamentals/assets/95337825/b2b9d42d-125e-4100-965f-b9d3447bd332)