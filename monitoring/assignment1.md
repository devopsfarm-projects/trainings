# Assignment 1: Monitor EC2, Linux & Windows Machines in Grafana Cloud (Unified Dashboard)

## 📅 Deadline: `___/___/2025`

## 🔧 Environment Setup

You must monitor the following **three machines** using **Alloy**, **Node Exporter**, and **cAdvisor**, and send all metrics to **Grafana Cloud**:

1. **Lab Linux Machine** — Already set up with Alloy + Node Exporter + cAdvisor
2. **AWS EC2 Linux Instance** — To be launched and configured
3. **Windows Machine** — To be configured with Alloy

---

## Part 1: Monitoring Setup

### 🟢 EC2 Linux Instance
- Launch EC2 (Ubuntu or Amazon Linux)
- Install:
  - Node Exporter
  - cAdvisor
  - Alloy (configured for Grafana Cloud)

### 🟢 Windows Machine
- Install Alloy
- Configure Alloy to send system metrics to Grafana Cloud

### 🟢 Lab Linux Machine
- Ensure it continues to send metrics via Alloy + Node Exporter + cAdvisor

---

## Part 2: Unified Dashboard Requirements

### Dashboard Name: `Multi-System Monitoring Dashboard`

Create **one dashboard** in Grafana Cloud that includes **all three machines**, clearly organized.

---

### Dashboard Layout

#### Section 1: Machine Overview (Top Summary)
- **Stat Panel × 3**: System Uptime (1 per machine)
- **Bar Chart**: Memory usage (%) comparison across 3 machines
- **Bar Chart**: Root disk usage (%) comparison

#### Section 2: Per-Machine Details

Use a **dashboard variable** named `$host` (based on the `instance` label).

Each panel below must support dynamic filtering by machine using `$host`:

| Panel Type    | Metric Example                                | Description                                       |
|---------------|------------------------------------------------|---------------------------------------------------|
| Gauge         | `100 - avg(irate(node_cpu_seconds_total{mode="idle"}[5m])) by (instance)` | CPU usage % (with thresholds)                    |
| Time Series   | `1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)` | Memory usage % over time                         |
| Time Series   | `irate(node_cpu_seconds_total{mode!="idle"}[5m])` | CPU usage trend                                  |
| Table         | `container_cpu_usage_seconds_total` (top 5)    | Top containers or processes by CPU               |
| Bar Chart     | `node_filesystem_avail_bytes`                 | Disk usage per mount point                       |
| Annotation    | System reboot (based on uptime or manual mark) | Reboot annotations on charts                     |

---

### Dashboard Features
- Dropdown **Variable `host`** — Filter by instance
- Dropdown **Variable `disk`** — Filter disk usage
- Default time range: **Last 1 hour**
- Auto-refresh: **Every 30 seconds**

---
### Dashboard Access
- You **must make the dashboard public** via **Grafana Cloud → Share → Public Access**.
- Copy the public URL and include it in your report.
---

## Part 3: Final Report

Submit a short report (PDF or Markdown):

1. Screenshot of your full dashboard (with each section)
2. CPU usage PromQL query with explanation
3. Challenges setting up EC2 & Windows monitoring
4. Key differences between Windows, EC2, and lab Linux metrics
5. **Public dashboard link**
---

## Submission Checklist

| Task                                          | Status |
|-----------------------------------------------|--------|
| EC2 instance launched & monitored              | [ ]    |
| Windows metrics configured with Alloy          | [ ]    |
| All metrics visible in Grafana Cloud           | [ ]    |
| One unified dashboard created                  | [ ]    |
| Required panels added with correct PromQL      | [ ]    |
| Variables for host and disk implemented        | [ ]    |
| Screenshot + report submitted                  | [ ]    |

---

