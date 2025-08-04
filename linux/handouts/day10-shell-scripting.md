## 🧑‍🏫 Shell Scripting for DevOps & SRE — Day 2
---

### 🎯 Objectives

* Handle arguments, arrays, and functions in advanced ways
* Automate tasks like monitoring, backup, log parsing, service restarts
* Introduce alerting and cron-based operations with logging
* Implement retries, error handling, and reporting

---

### ⏱️ **Session Duration**: 2.5–3 hours

---

### 🧮 **1. Enhanced Arguments Demo (15 mins)**

```bash
#!/bin/bash
if [ $# -lt 2 ]; then
  echo "Usage: $0 <filename> <pattern>"
  exit 1
fi

file=$1
pattern=$2

echo "Searching for '$pattern' in $file"
grep "$pattern" "$file"
```

💡 **Use Case**: Parse logs dynamically for incidents

---

### 🔁 **2. Advanced Disk Usage Monitor with Alert (30 mins)**

```bash
#!/bin/bash
threshold=80
mail_recipient="sre-team@example.com"
log="/var/log/disk_check.log"
date >> $log

df -H | grep -vE '^Filesystem|tmpfs' | while read line; do
  usage=$(echo $line | awk '{ print $5 }' | sed 's/%//g')
  mountpoint=$(echo $line | awk '{ print $6 }')

  if [ "$usage" -ge "$threshold" ]; then
    msg="⚠️ Disk usage on $mountpoint is ${usage}%"
    echo "$msg" | tee -a $log
    echo "$msg" | mail -s "Disk Alert: $mountpoint" $mail_recipient
  fi
done
```

💡 Real-world: Run via cron every 15 mins on critical nodes.

---

### 🧪 **3. Dynamic Backup Script with Exclusions and Logging (25 mins)**

```bash
#!/bin/bash
src="/var/www"
dest="/backup/web_$(date +%F_%H-%M).tar.gz"
exclude_list="/opt/scripts/backup_exclude.txt"
log="/var/log/backup.log"

echo "Starting backup: $(date)" >> $log

tar --exclude-from=$exclude_list -czf $dest $src 2>>$log

if [ $? -eq 0 ]; then
  echo "✅ Backup successful: $dest" >> $log
else
  echo "❌ Backup failed: $(date)" >> $log
fi
```

📄 `backup_exclude.txt` example:

```
/var/www/tmp
/var/www/cache
```

---

### 🔍 **4. Intelligent Log Analysis Script with Report (30 mins)**

```bash
#!/bin/bash
logfile="/var/log/syslog"
report="/tmp/error_report_$(date +%F).txt"

echo "Error Report - $(date)" > $report
echo "------------------------" >> $report

grep -iE "error|fail|critical" $logfile | sort | uniq -c | sort -nr >> $report

# Optional: Send to email or Slack webhook
echo "Error report saved to $report"
```

💡 Use Case: Daily error summary for incidents.

---

### 🔧 **5. Retry & Auto-Restart Services with Status Report (30 mins)**

```bash
#!/bin/bash
services=("nginx" "docker" "sshd")
report="/tmp/service_check_$(date +%F_%H-%M).log"

echo "Service Health Check - $(date)" > $report

for svc in "${services[@]}"; do
  systemctl is-active --quiet $svc
  if [ $? -ne 0 ]; then
    echo "❌ $svc is down. Attempting restart..." | tee -a $report
    systemctl restart $svc
    sleep 3
    systemctl is-active --quiet $svc && echo "✅ $svc restarted successfully" >> $report || echo "❌ $svc restart failed!" >> $report
  else
    echo "✅ $svc is running" >> $report
  fi
done
```

📬 Schedule via cron + mail the log to SRE mailbox.

---

### 🔁 **6. Cron with Logging and History (10 mins)**

```bash
# crontab -e

*/10 * * * * /opt/scripts/check_services.sh >> /var/log/check_services.log 2>&1
```

💡 Tip: Rotate logs with `logrotate.d` or archive weekly via another shell script.

---

### 🔐 **7. Secure and Reusable Best Practices (10 mins)**

* Use full paths (`/usr/bin/grep`)
* Check return codes (`$?`) after critical steps
* Use `set -euo pipefail` for safety
* Redirect errors to a log file (`2>>error.log`)
* Use functions for modular scripts
* Document parameters and usage inside the script

---

### 🧠 **Homework Assignments (Advanced)**

1. **Failover Script**: Check service health, if down, update route/DNS or fallback IP
2. **Auto-rotate Logs**: Move logs >10MB to archive folder with timestamp
3. **Uptime Summary Script**: Generate a report of system uptime across 3 machines via SSH loop
4. **Monitor Public Website**: Script that pings or curl-checks a public endpoint, retries 3x before alert
5. **Dynamic User Creation**: Create users from CSV file with random passwords and assign to groups
