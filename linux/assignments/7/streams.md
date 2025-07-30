# 🧪 DevOps Linux Shell Scripting Assignment - Day 1

👨‍🏫 **Trainer Note:**  
Welcome to your first real-world assignment. In this 2-hour hands-on session, you'll practice core shell utilities like `grep`, `awk`, `sed`, `cut`, `sort`, and `uniq` using realistic DevOps and SRE scenarios. Make sure to complete each part and submit your output files where required.

---

## 🗂 Part 1: Log Analysis (30 minutes)

📝 **File:** `nginx-access.log`

```bash
10.1.1.1 - - [29/Jul/2025:10:20:15 +0000] "GET /index.html HTTP/1.1" 200 1024
10.1.1.2 - - [29/Jul/2025:10:21:15 +0000] "GET /favicon.ico HTTP/1.1" 404 512
10.1.1.3 - - [29/Jul/2025:10:22:15 +0000] "POST /api/login HTTP/1.1" 200 2048
10.1.1.1 - - [29/Jul/2025:10:23:15 +0000] "GET /dashboard HTTP/1.1" 500 128
```

🔧 **Tasks:**

1. Extract status codes (e.g., `200`, `404`) using `awk` or `cut`.
2. Count each status code’s frequency using `sort` and `uniq -c`.
3. List **unique IPs** that accessed the server.
4. Display only lines with status `500`.
5. Extract all URLs accessed by users.

💡 *Hint:* Use `awk '{print $9}'`, `cut -d ' ' -f9`, `sort`, `uniq`, and `grep 500`.

---

## ⚙️ Part 2: Configuration Editing with `sed` and `cut` (30 minutes)

📝 **File:** `app.env`

```env
APP_NAME=myapp
PORT=8080
DEBUG=True
DATABASE_URL=postgres://admin:pass@localhost:5432/mydb
```

🔧 **Tasks:**

1. Replace `DEBUG=True` with `DEBUG=False` using `sed`.
2. Change the port to `9090`.
3. Extract and print **only the DB host** (`localhost`) using `cut`.
4. Mask the password (`pass`) with `********` in the `DATABASE_URL`.

💡 *Hint:* Use `sed -i`, regex grouping, and `cut -d '@'`.

---

## 📊 Part 3: System Resource Filtering (30 minutes)

📝 **Simulated File 1:** `df-sample.txt`

```bash
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   25G   25G  50% /
/dev/sdb1       100G   90G   10G  90% /data
```

📝 **Simulated File 2:** `top-sample.txt`

```bash
PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
1023 root      20   0  500000  15000   2000 R  55.5  1.2   0:10.23 python
1044 www-data  20   0  300000  10000   1500 S  12.1  0.8   0:03.02 nginx
```

🔧 **Tasks:**

1. In `df-sample.txt`, print partitions with usage **greater than 80%**.
2. In `top-sample.txt`, extract lines where CPU usage is more than **50%**.
3. Print only `PID`, `%CPU`, and `COMMAND` columns using `awk`.

💡 *Hint:* Look for `Use%` column in `df` and use `$9 > 50` in `awk`.

---

## 📈 Part 4: Monitoring Data Aggregation (30 minutes)

📝 **File:** `metrics.txt`

```
timestamp=2025-07-29T10:00:00 cpu=45 memory=2012MB
timestamp=2025-07-29T10:05:00 cpu=72 memory=3200MB
timestamp=2025-07-29T10:10:00 cpu=81 memory=2100MB
timestamp=2025-07-29T10:15:00 cpu=34 memory=1200MB
```

🔧 **Tasks:**

1. Extract all timestamps where `cpu > 70` using `awk`.
2. Remove `MB` suffix from memory and print numeric value using `sed`.
3. Calculate average CPU usage using `awk`.

💡 *Hint:* Use regex in `sed`, and sum/count logic in `awk`.

---

## 📤 Submission Guidelines

- Create a directory called `linux-assignment-01`.
- Store your scripts or commands as individual `.sh` or `.txt` files.
- Redirect final outputs (if applicable) to `.out` files.
- Submit the folder to your GitHub repo or class portal.

---

✅ **Trainer's Tip:**  
Use `watch`, `tail`, and `head` if you want to explore more. Don’t just run the command — **understand why and how**. These exercises simulate what you’ll actually do in monitoring, debugging, and automation.

---

**Duration:** 🕑 2 Hours  
**Level:** Beginner to Intermediate  
**Topics:** `grep`, `awk`, `sed`, `cut`, `sort`, `uniq`, config editing, log analysis
