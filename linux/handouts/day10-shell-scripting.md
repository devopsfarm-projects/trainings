### 🎯 Objectives

* Handle arguments, arrays, functions
* Introduce monitoring, log parsing, backup scripts
* Schedule scripts using `cron`

---

### ⏱️ **Session Duration**: 2.5 hours

---

### 🧮 **1. Command-line Arguments (15 mins)**

```bash
#!/bin/bash
echo "Target file: $1"
wc -l $1
```

💡 **Use Case**: Used in automation jobs that take filename or path as arguments, e.g., processing logs.

---

### 🔁 **2. Real DevOps Script: Check Disk Usage (20 mins)**

```bash
#!/bin/bash
threshold=80
usage=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')

if [ "$usage" -gt "$threshold" ]; then
  echo "Disk usage is above threshold! ($usage%)"
  # Send alert or email
else
  echo "Disk usage is under control ($usage%)"
fi
```

✅ Use in production for `/`, `/var`, or `/data`.

---

### 🧪 **3. Backup Script (25 mins)**

```bash
#!/bin/bash
src="/var/www/html"
dest="/backup/html_$(date +%F).tar.gz"

tar -czf $dest $src

if [ $? -eq 0 ]; then
  echo "Backup successful: $dest"
else
  echo "Backup failed!"
fi
```

💡 Real world usage: Run via cron every night on production web servers.

---

### 🔍 **4. Log Analysis Script (25 mins)**

```bash
#!/bin/bash
log="/var/log/syslog"
grep -i "error" $log | tail -n 10
```

📈 **Enhanced Version**: Count occurrences of different error types

```bash
awk '/ERROR/ { print $NF }' /var/log/app.log | sort | uniq -c | sort -nr
```

💡 SRE use case: Create lightweight alerting for log patterns before integrating with ELK or SumoLogic.

---

### 🔧 **5. Script with Functions (20 mins)**

```bash
#!/bin/bash

check_service() {
  systemctl is-active --quiet $1 && echo "$1 is running" || echo "$1 is NOT running"
}

for svc in nginx docker sshd; do
  check_service $svc
done
```

📦 Makes it modular and easy to reuse.

---

### 🕘 **6. Scheduling with Cron (10 mins)**

```bash
crontab -e

# Run backup at 2am daily
0 2 * * * /opt/scripts/backup.sh
```

---

### 🧠 **7. Scripting Best Practices (10 mins)**

* Use `#!/bin/bash` explicitly
* Always handle exit codes (`$?`)
* Use logging (`logger`, `echo`)
* Avoid hardcoding paths

---

### 📘 **Day 2 Homework**

* Script to check if given IP is reachable (ping check)
* Script to rotate logs (move to archive if size > 10MB)
* Script to check and restart failed services (use `systemctl`)

---
