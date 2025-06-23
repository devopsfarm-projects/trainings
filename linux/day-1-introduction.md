# Linux OS Distributions

## Kali Linux
Kali Linux is a specialized Linux distribution primarily developed as a replacement for the earlier Backtrack distribution. It is designed specifically for penetration testing and security auditing. Kali Linux is known for its comprehensive suite of tools that facilitate successful penetration testing tasks.

## Backtrack
Backtrack was a powerful platform that provided a wide range of tools for successful penetration testing. It served as the precursor to Kali Linux and laid the foundation for advanced security testing methodologies.

## Knoppix Linux
Knoppix Linux is an operating system based on Debian, designed to run directly from a CD/DVD or a USB flash drive. It offers a portable and flexible environment, making it ideal for various purposes, including testing and system recovery.

## Debian
Debian is an open-source operating system that utilizes the Linux kernel. It is known for its stability, security, and adherence to free software principles. Many Linux distributions, including Kali Linux, are based on Debian.

## Evolution to Kali Linux
Kali Linux evolved from Backtrack, incorporating advancements in security tools, usability, and stability. It represents a revamped version of the renowned Backtrack distribution, catering specifically to the needs of security professionals and enthusiasts.


## Development and Release
Kali Linux 1.0 was officially released in 2013. It marked a significant milestone in the development of penetration testing distributions, offering advanced, robust, and stable tools for security professionals.

## Creators
Kali Linux was developed by Mati Aharoni and Devon Kearns of Offensive Security. Their expertise and contributions have been instrumental in shaping Kali Linux into one of the most preferred penetration testing distributions.

## Kernel
Kernel is a computer program at the core of a computer operating system with complete control over everything in the system.

It faciliates interaction or interface between hardware and software components.

The kernel take responsibility for deciding at any time which at the many running programs should be allocated to the processors.

Ram is used to store both programs instruction and data. the kernel is responsible for deciding which memory each process can use.

It handles peripheral slike keyboards, monitors printer and speaker.
Types of Kernel

## 1.] Monolithic kernel

![Monolithic-Architecture](https://github.com/MaheshShukla1/Linux-Fundamentals/assets/95337825/94b41cb1-9eb6-44f5-a7f4-8de226ce12a1)

## 2.] Micro kernel

![Microkernel](https://github.com/MaheshShukla1/Linux-Fundamentals/assets/95337825/837f85ae-5dd3-4bcd-825b-60146e257008)

## 3.] Hybrid kernel

![Hybrid-Kernel-Architecture-23](https://github.com/MaheshShukla1/Linux-Fundamentals/assets/95337825/869687f1-cbee-4bc1-9d96-8d1f32c2c40f)

# Linux Fundamentals
## Kernel
The kernel is a core component of a computer operating system, providing complete control over system resources. It facilitates interactions between hardware and software components, allocating resources and managing processes efficiently.

## RAM (Random Access Memory)
RAM is used to store program instructions and data temporarily. The kernel manages memory allocation, ensuring that each process receives the necessary memory resources for execution.

## Shell
The shell is an interface that allows users to interact with the Linux system through commands. It interprets user commands and executes them, serving as a bridge between users and the operating system.

## Types of Shells
Bash Shell (Bourne Again Shell): Developed for the GNU project, it is the default standard shell in most Linux distributions. The prompt character ($) indicates its usage.

Bourne Shell: The original Unix shell, written by Bill Joy at UC Berkeley. It was the first shell to appear on Unix systems and is often installed as /bin/sh.

Csh (C Shell): Known for its similarity to the C programming language syntax, it is preferred by some users, especially network administrators comfortable with C programming concepts. The prompt character (%) indicates its usage.

## Linux File System Hierarchy (FHS)
The File System Hierarchy Standard (FHS) defines the directory structure and organization of files in a Linux system. It ensures consistency across distributions and provides a standardized framework for file placement.

## Key Directories
/bin: Contains essential commands accessible to both system administrators and regular users.

/boot: Stores files required for the boot process, including the kernel and bootloader configurations.

/dev: Houses device files representing hardware devices, facilitating communication between the operating system and hardware components.

/etc: Stores system-wide configuration files, including network settings, user configurations, and application settings.

/home: Contains user home directories, providing storage for user-specific files, settings, and configurations.

/lib: Contains shared library files necessary for booting the system and executing commands in the root file system.

/media: Acts as a mount point for removable media devices such as USB drives and optical discs.

/mnt: Provides a temporary mount point for file systems, allowing administrators to mount external or temporary file systems as needed.

/opt: Typically used for optional software packages, providing a separate directory for additional applications not included in the core system.

/root: Home directory for the root user, the superuser with unrestricted access to system resources.

/sbin: Contains essential system administration utilities, often used for booting, recovery, and system repair tasks.

/srv: Stores site-specific data served by the system, such as website files or data accessible to network services.

/tmp: Houses temporary files used by programs and processes, with contents typically cleared on system reboot.

/usr: Contains shareable read-only data, including applications, libraries, and user-related files used by multiple users.

/var: Stores variable data files, including logs, administrative data, temporary files, and database files used by system processes and applications.

## linux file types

When navigation the linux file system you are sure to encounter different file types.

There are different file types within the linux program system.

- -: regular file
- d: directory
- c: character device file
- b: blocked device file 
- s: local socket file
- p: named pipe 
- l: symbolic link

## Regular files

Most common file types found on the linux system you can create regular file with touch command.

## Directory files

Directory is the second most common file type found in linux. directory can be created with the mkdir.

## Character and block device files

character and block device files allow users and programs to communicate with hardware peripheral devices.

## local socket file

local domain sockets are used for communication between processes generally, they are used by services such as x windows. spylog and etc.

In kali linux c and other linux systems, local socket files provide a mechanism for processes on the same machine to communicate with each other efficiently. unlike network socket that use the TCP/IP model for communication across a network , local sockets facilitate inter-process communication (IPC) within the system itself.

## Key characteristics

File based:- local sockets exist as regular files with the sock extension in the file system, typically located in the directories like /var/run or  /tmp.

Bidirectional:- they enable two way data exchange between processes.

Lightweight:- compared to network sockets, local sockets offer faster and more resource-efficient communication due to the absence of network overhead.

Example scenario:- Imagine you have a web server (like apache) running in kali linux. It might use a socket file (e.g) /var/run/apache2.sock) to allow web applications (like php scripts) to correct and exchange communication within the system itself, improving performance.

## Common uses

Database servers:- mysql, postgresql  and other database servers often use local sockets for client connection.

Windows system:- x window system (x11) leverages local sockets for communication between the x server and client application.

wshom applications:- developers can create programs that utilize local sockets for tailored IPC needs within their software.


## Accessing local sockets file

Process listing:- tools like ==lsof== or ==netstat== can display information about open sockets including local socket file. for example lsof+g /var/run/apache2.sock would show processes connected to the apache sockets.

Permissions:- local sockets have ownership and permission settings that control which users or processes can access them.

Remember that local socket files are not intended for communications across networks. they are specifically designed for efficient inter-process communication within a single system.

## Named pipe

Named pipe allows communication between two local processes. they can be created by the mknod command and removed with the rm command.

Here's what a named pipe also called FIFO is in kali linux.

Inter process communication

It's a special file that allow programs to exchange data.

like a pipe, but with a name

Unlike regular pipes, named pipes exist in the filesystem within a name, so multiple programs can access them.

First in first out (FIFO
data goes first, come out first.
Created with mkfifo
use this command to create a name pipe.

## Symbolic link

with symbolic link an administrator can assign a file or directory multiple identifies

Imagine a symbolic link in kali linux like a shortcut on your computer. instead of copying a whole life. This way you can access the file from the shortcut just as easily . but you save space by not having duplicates.

Here's what makes symbolic links ready.

Easy access:- they provide quick access to files or folders in different locations without moving the originals.

Save spaces:- no duplicate files means less storage used.

Flexibility:- they can point to files anywhere on your system, even on different drives.

Think of it like having a fancy bookmark that takes you right to the page you  want in a book, no matter where you open the book.

## Control operators

with the help of control operators you can put more than one command in the command line. It helps in performing function.
 ; semicolon

ampersand &

When a line and with an ampersand & the shell will not wait for the command to finish.

you will get your shell prompt back and the command is executed in the background. you will get a message when the command has finished executing in background.

Double ampersand &&

The shell will interpret && as a logical AND. when using the second command is executed only if the first one succeeds. (return as zero exit status)

Panel sign '#'

Everything written after a pound sign (#) is ignored by the shell. This is useful to write a shell comment, but has no influence on the command execution or shell expansion.

## I/O redirection

This feature of the command like enables you to redirect the input and/or input of commands from and/or to files.

>> append "it is cold today" >> simple.txt


## Filter and pipes

When a program takes its input from another program it performs some operation on that input and writes the result to the standard input. it is referred to as its filter.

## Grep command

The Grep command Searches a file for lines that have a certain pattern. The syntax is $ grep pattern file (s)

The name "grep" cores from the (a unix line editor) command  g/r/e/p which means "Globally search for regular expressions and print all lines containing it".

## Pipe command

more than two commands may be linked up to a pipe. "|"

## Process management

Whenever you issue a command in unix, it creates or starts a new process. When you tried out this command to list the directory contents, you started a process. is an instance of a running program.

Starting a process

when you start a process (run a commands), there are two ways you can run it

Foreground process

Background process

In kali linux, just like any other computer system, process management is all about juggling the programs that are running. Imagine you have a bunch of cooks in a kitchen (The programs), all working on different dishes (tasks). 

Process management helps you see who is doing what:- you can check which programs are running and what resources they're using memory. with commands like PS and TOP.

Take control

You can start, stop , or prioritize programs. need a program to focus on its tasks, you can adjust its priority. Is a program running slowly? you can stop it to free up resources for others.

## Foreground services

Needs your attention and stays active even when you leave the app.

## Background services

Works silently in the background without needing your immediate attention.

## Scripting introduction

A shell script is a computer program designed to be run by the unix/shell. It is a file that contains ASCII text data files, text files, data sets.

Absolutely! Scripting in kali linux is like putting together a recipe for your computer instead of typing out commands one by one. you write them down in a step list. This lets you automate repetitive tasks, like checking security vulnerabilities on multiple machines.
Ingredients (commands):- you use the command you already know from kali linux.

Recipe  (scripts):- you write these commands in a text file, like a grocery list.

Cook book (shell):- Kali Linux uses a program called  a "shell" to follow your recipe.

Cooking (running):- When you run the script the shell follows your instruction automating the task.

Note
This saves you time and effort, especially when you need to do same things over and over.

## Root system
This is also called superuser and would have complete and untattered control of the system. A Superstar can run any command without any restriction. 

This user should be assured as a system administrator.

## Service accounts
Service accounts are created by installation packages when they are installed. These accounts are used by services to run processes and execute functions. These accounts are not used in routine work.

## User account
user accounts provide interactive access to the system for users and groups of users.

Linux supports a concept of group account which logically groups a number of accounts. every account would be a part of another group account. 

A linux group plays an important role in handling file permission and process management.

Managing users and groups.
There are four main user administration files.

## /etc/passwd
keep the user account and password information the files hold the majority of information about accounts on the unix system.

## /etc/shadow
holds the encrypted password of the corresponding account not all the system support this file.

## /etc/group
This file contain the group information for each account

## /etc/gshadow
This file contain secure group account information

## Managing user and groups
user add:- adds an account to the system.
user mod:- modifies account attributes
userdel:- delete account from the system
group add:- modifies group attributes
groupdel:- remove group from the system
Short notes

## Linux Fundamentals
Kernel:- Core program controlling the system, managing hardware and software resources.

RAM (Random Access Memory):-  Stores program instructions and data for temporary use.

Shell:-  Interface for users to interact with the system using commands.
Types:- Bash (most common), Bourne Shell, Csh

## Linux File System Hierarchy

FHS (File System Hierarchy Standard):-  Defines directory structure and file placement for consistency across distributions.

## Common Directories::
    /bin:- Essential commands for all users (e.g., cat, ls, cp).
    /boot:-  Files required for the boot process (e.g., kernel).
    /dev:- Device files representing hardware devices.
    /etc:- System-wide configuration files.
    /home:- User home directories containing personal files and settings.
    /lib:- Shared libraries needed by programs in **/bin** and **/sbin**.
    /media:- Mount point for removable media (e.g., USB drives).
    /mnt:- Temporary mount point for file systems.
    /opt:- Optional application software packages.
    /root:- Home directory for the root user.
    /sbin:-  System administration utilities.
    /srv:- Site-specific data served by the system (e.g., website files).
    /tmp:- Temporary files, deleted on reboot.
    /usr:- Read-only shareable data, containing applications and user files.
   /var:- Variable data files (e.g., logs, spool data, cache).
   /proc:- Special file system providing information about running      processes.
   /lost+found:- Recovered file fragments from crashes or errors.
    /run:- Temporary storage for system processes (e.g., PIDs, device files).

## Linux File Types

Regular File:- Most common type (e.g., text files, documents).
Directory:- Contains other files and subdirectories.
Special Files:- Represent hardware devices (character, block).
Sockets:- Facilitate communication between processes.
Named Pipes (FIFOs):- Allow data exchange between two processes.
Symbolic Links:- Shortcuts to files or directories elsewhere.

## Control Operators

Semicolon (;):- Execute multiple commands sequentially.
Ampersand (&):- Run a command in the background.
Double Ampersand (&&):- Execute the second command only if the first succeeds.
Hash (#):- Comment line, ignored by the shell.

## I/O Redirection

Redirects input or output of commands to/from files (e.g., >> to append).

## Filters and Pipes
Filters:- Process data from another program (e.g., grep).
Pipes (|):- Send output of one command as input to another.


## Process Management
Processes:- Instances of running programs.
Foreground Processes:- Run in the terminal and require your attention.
Background Processes:- Run silently in the background.
Commands:- ps (list processes), top (monitor process activity).

## Scripting
Shell Scripts:- Automate repetitive tasks using a series of commands.

## User Accounts and Groups

Root:- Superuser with unrestricted access to the system.
Service Accounts:- Used by services to run processes.
User Accounts:- Provide access to the system for individual users or groups.
Groups:- Logically group accounts for permission management.

## Managing Users and Groups
Commands:
    - useradd: Add a user account.
    - usermod: Modify user attributes.
    - userdel: Delete a user account.
    - groupadd: Add a group.
    - groupmod: Modify group attributes.
    - groupdel: Delete a group.

## Additional Notes

-/etc/passwd:-  Stores user account information (excluding passwords).
-/etc/shadow:- Stores encrypted user passwords (on systems that support it).
-/etc/group:- Contains group information for each account.
-/etc/gshadow:- Stores secure group account information (on systems that support it).

This revised version condenses the information while maintaining clarity. I hope it's helpful!


![logo_1](https://github.com/MaheshShukla1/Linux-Fundamentals/assets/95337825/5414366c-e264-4458-b7c7-a46a2b417379)

