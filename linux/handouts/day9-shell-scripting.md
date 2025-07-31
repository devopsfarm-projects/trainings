### 🎯 Objectives

* Understand basic syntax and control structures
* Automate tasks like user creation, service checks, and file management
* Prepare scripts that can be scheduled via `cron`

---

### ⏱️ **Session Duration**: 2 to 2.5 hours

---

### 🧠 **1. What is Shell Scripting? (10 mins)**

* A shell script is a program written for the shell to automate tasks.
* Widely used in DevOps/SRE for provisioning, monitoring, backups, and deployments.

✅ **Trainer Example**:

> "In our environment, we use shell scripts to:
>
> * Check whether critical services like nginx or docker are running
> * Rotate logs every night using a cronjob
> * Parse `/var/log/syslog` for alert patterns"

---

### 🧪 **2. Your First Script (10 mins)**

```bash
#!/bin/bash
echo "Welcome to DevOps Shell Scripting"
hostname
date
```

✅ **Use Case**: Can be used in a post-deployment verification step.

---

### 🔣 **3. Variables and Input (15 mins)**

```bash
#!/bin/bash
server="web01"
echo "Checking server: $server"

read -p "Enter your environment (dev/stage/prod): " env
echo "Deploying to $env environment"
```

💡 Use Case:

* Define `env`, `region`, or `instance_type` before running Terraform or Ansible scripts.

---

### 🔀 **4. Conditional Logic (20 mins)**

```bash
#!/bin/bash
read -p "Enter service name: " svc

if systemctl is-active --quiet "$svc"; then
  echo "$svc is running"
else
  echo "$svc is NOT running"
fi
```

💡 **Use Case**: Used by SREs for service health checks. Integrate with Prometheus blackbox exporters or alertmanager hooks.

---

### 🔁 **5. Loops for Automation (20 mins)**

```bash
#!/bin/bash
services=("nginx" "sshd" "docker")

for svc in "${services[@]}"; do
  systemctl is-active --quiet $svc && echo "$svc is running" || echo "$svc is NOT running"
done
```

💡 **Use Case**: Nightly service audit script run via cron.

---

### 📘 **6. Homework for Day 1**

* Script to create multiple users from a list
* Script to find and delete `.log` files older than 7 days
* Explore `man test` and `man bash` pages
