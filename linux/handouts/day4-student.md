# DevOpsFarm IT Solutions
## Linux for DevOps – Day 4 Student Handout (Detailed)

---

### Topics Covered:
1. Users and Groups Management  
2. Process Management  
3. Service Management (Systemd Basics)  
4. Disk Usage & Monitoring (Optional)

---

## 1. USERS & GROUPS MANAGEMENT

**whoami**  
> Shows the current logged-in user.  
`whoami`

**id**  
> Displays UID, GID, and groups of the current user.  
`id`

**groups**  
> Lists all groups the user is part of.  
`groups`

**useradd <username>**  
> Adds a new user to the system.  
`sudo useradd devuser`

**groupadd <groupname>**  
> Creates a new group.  
`sudo groupadd devgroup`

**usermod -aG <group> <user>**  
> Adds a user to a group (append mode).  
`sudo usermod -aG devgroup devuser`

**passwd <username>**  
> Sets or changes the password for a user.  
`sudo passwd devuser`

**su - <username>**  
> Switches to another user.  
`su - devuser`

**sudo -i**  
> Starts a root shell using sudo.

**/etc/passwd** - File that stores user account information.  
**/etc/group** - File that stores group info.

---

## 2. PROCESS MANAGEMENT

**ps aux** - Displays all running processes with detailed info.  
`ps aux`

**ps -ef** - Alternate format for viewing processes.  
`ps -ef`

**top** - Live updating view of system processes.

**htop** - Enhanced version of top (may need to install it).  
`htop`

**sleep 1000 &** - Runs a process in the background.

**jobs** - Shows background jobs.

**fg %1** - Brings job 1 to the foreground.

**kill <PID>** - Terminates a process by its PID.  
`kill 1234`

**killall <name>** - Terminates all processes by name.  
`killall sleep`

**nice -n <value> <command>** - Starts a command with a specific priority.  
`nice -n 10 sleep 1000`

**renice -n <value> <PID>** - Changes priority of a running process.  
`renice -n 5 1234`

---

## 3. SERVICE MANAGEMENT (SYSTEMD)

**systemctl status <service>** - Checks the status of a service.  
`systemctl status ssh`

**systemctl start/stop/restart <service>** - Starts, stops, or restarts a service.

**systemctl enable/disable <service>** - Enables or disables a service on boot.

**journalctl -u <service>** - Views logs related to a service.  
`journalctl -u ssh`

---

## 4. DISK & MEMORY MONITORING

**df -h** - Shows disk usage in human-readable format.  
`df -h`

**du -sh *** - Shows size of each item in current directory.  
`du -sh *`

**free -m** - Displays memory usage in megabytes.  
`free -m`

**uptime** - Shows system uptime and load average.  
`uptime`

---

## ✅ Assignment

1. Create a new user and assign it to a group.  
2. Run a background process (like sleep), monitor and kill it.  
3. Restart a service and check its status and logs.  
4. Use `df`, `du`, and `free` to analyze disk and memory usage.