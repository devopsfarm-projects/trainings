
# 🧪 Linux for DevOps – 5-Day Assignment

## 📅 Duration: Approx. 4–5 hours

---

## 🔹 Day 1: Linux Introduction & File System Basics

### 1. Directory Structure Overview

Explain the purpose of each directory:
- `/bin` -
- `/etc` -
- `/var` -
- `/home` -
- `/opt` -
- `/usr` -

### 2. Practice Commands

```bash
mkdir -p ~/devops_assignment/day1/scripts
cd ~/devops_assignment/day1
touch linux_notes.txt
mkdir ~/testdir
pwd
ls -l
```

🎯 **Task**: Capture screenshot of `ls -l` output in both folders.

---

## 🔹 Day 2: Users, Groups & Permissions

### 1. User & Group Management

```bash
sudo groupadd devops
sudo useradd -m -G devops alice
sudo useradd -m -G devops bob
sudo passwd alice
sudo passwd bob
```

### 2. File Permissions

```bash
cd ~/devops_assignment/day2
touch secret.txt
chmod 600 secret.txt
chown alice:devops secret.txt
```

🎯 **Task**: Show output of `ls -l` and `groups alice`

---

## 🔹 Day 3: Package Management, Viewing Files

### 1. Install & View Packages

```bash
sudo apt update
sudo apt install htop curl tree vim
apt-cache show curl
```

### 2. View System Files

```bash
cat /etc/passwd | head -5
less /etc/passwd
tail -f /var/log/syslog &
```

🎯 **Task**: Document usage of each command with screenshots/output.

---

## 🔹 Day 4: Editors, History, Commands

### 1. Text Editors

- Open `bio.txt` in `vim`, write about yourself, and save.

```bash
vim bio.txt
nano shortbio.txt
```

### 2. History and Aliases

```bash
history | tail -20
echo "alias ll='ls -l'" >> ~/.bash_aliases
source ~/.bash_aliases
```

🎯 **Task**: Show `bio.txt` content and last 10 commands from history.

---

## 🔹 Day 5: Services, Cron, Custom Script

### 1. View System Services

```bash
systemctl list-units --type=service
systemctl status ssh
```

### 2. Cron Job

```bash
crontab -e
# Add line below:
*/5 * * * * echo "Date: $(date)" >> /tmp/date.log
```

### 3. Script to Service

Create script `/opt/heartbeat.sh`:

```bash
#!/bin/bash
while true; do
  echo "I'm alive at $(date)" >> /var/log/heartbeat.log
  sleep 30
done
```

Make it executable:

```bash
chmod +x /opt/heartbeat.sh
```

Create service file:

```ini
# /etc/systemd/system/heartbeat.service
[Unit]
Description=Heartbeat Logger

[Service]
ExecStart=/opt/heartbeat.sh
Restart=always
User=root

[Install]
WantedBy=multi-user.target
```

Enable service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable heartbeat
sudo systemctl start heartbeat
```

🎯 **Task**:
- Show service status: `systemctl status heartbeat`
- Show logs: `journalctl -u heartbeat --since "5 minutes ago"`

---

## ✅ Submission Checklist

- assignment.md file with all commands and answers
- screenshots of key steps
- shell scripts used
- compressed folder: `assignment.zip`

