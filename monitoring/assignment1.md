# 🎯 Assignment: Monitor EC2, Linux & Windows Machines in Grafana Cloud (Unified Dashboard)

## 📅 Deadline: `___/___/2025`

---

## 🔧 Overview

You are required to monitor **three systems** using **Alloy**, **Node Exporter**, and **cAdvisor**, and build a **single unified dashboard** on **Grafana Cloud**. The dashboard must provide insights into system and container-level metrics for each machine and be publicly viewable.

---

## 🌐 Monitored Systems

| Machine             | Setup Tasks                                                                 |
|---------------------|------------------------------------------------------------------------------|
| **Lab Linux Machine**  | Already set up (Alloy + node_exporter + cAdvisor); must run 2+ containers |
| **EC2 Linux Instance** | Launch instance, install Alloy + exporters, run 2+ containers              |
| **Windows Machine**    | Install and configure Alloy to send metrics to Grafana Cloud              |

---

## ⚙️ Part 1: Setup Instructions

### 1. EC2 Linux Instance
- Launch a **t2.medium or larger** EC2 instance (Ubuntu preferred)
- Open ports if needed (only for setup, then disable!)
- Install:
  - `node_exporter`
  - `cadvisor`
  - `alloy` (send metrics to Grafana Cloud)
- Run at least **two containers** (`nginx`, `redis`, or similar) using Docker

### 2. Windows Machine
- Install **Alloy for Windows**
- Configure it to send CPU, memory, and disk metrics to Grafana Cloud
- (You can skip containers for this machine)

### 3. Lab Linux Machine
- Ensure Alloy + node_exporter + cAdvisor are running
- Start at least **two containers** if not already running

---

## 📊 Part 2: Unified Grafana Dashboard

### 📛 Dashboard Name: `Multi-System Monitoring Dashboard`

This **one single dashboard** must monitor **all three machines**, structured into sections:

---

### 🧩 Section A: Machine Summary

| Panel Type | Description |
|------------|-------------|
| **Stat × 3** | Uptime for each machine |
| **Bar Chart** | Compare memory usage (%) across 3 machines |
| **Bar Chart** | Compare root disk usage (%) across 3 machines |

---

### 🧩 Section B: Machine Drilldown (Dynamic with Variables)

> Use a dashboard **variable named `$host`** (`instance` label)

| Panel Type    | Description                                         | PromQL Hint |
|---------------|-----------------------------------------------------|-------------|
| Gauge         | CPU Usage %                                          | `100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)` |
| Time Series   | Memory usage over time                               | `(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes))` |
| Time Series   | CPU usage over time                                  | `irate(node_cpu_seconds_total{mode!="idle"}[5m])` |
| Table         | Top 5 containers by CPU usage                        | `topk(5, rate(container_cpu_usage_seconds_total[5m]))` |
| Bar Chart     | Disk usage per mount point                           | `node_filesystem_size_bytes - node_filesystem_avail_bytes` |
| Annotation    | Manual annotation or auto-annotation for reboots     | (Use uptime drop logic or manual) |

---

### 🎛 Dashboard Features
- Variable: `$host` — dropdown of instance label
- Variable: `$disk` — mount point filter
- Refresh interval: **30s**
- Default time range: **Last 1 hour**
- Use **descriptive titles** and **panel units**
- Apply **color thresholds** (e.g., red above 80% usage)

---

## 🌍 Part 3: Make Dashboard Public

- In Grafana Cloud:
  - Click `Share`
  - Enable **public access** for the dashboard
  - Copy the **public link**
  - Add it in your report

---

## 📝 Part 4: Report Submission (Markdown or PDF)

Your report must include:

1. Screenshot of full dashboard (all panels visible)
2. PromQL query used for CPU usage (with explanation)
3. List of container names you ran on each Linux system
4. Public dashboard link
5. Any issues faced and how you resolved them
6. Key observations across the 3 systems

---

## Final Checklist

| Task                                               | Done? |
|----------------------------------------------------|--------|
| EC2 instance launched and monitored                | [ ]    |
| Windows machine metrics configured via Alloy       | [ ]    |
| Containers running on EC2 and Lab Linux            | [ ]    |
| cAdvisor metrics verified for both Linux machines  | [ ]    |
| All metrics visible in Grafana Cloud               | [ ]    |
| Single dashboard created and organized             | [ ]    |
| Required panels and filters added                  | [ ]    |
| Variables and annotations implemented              | [ ]    |
| Dashboard made publicly viewable                   | [ ]    |
| Report created with screenshots + queries + link   | [ ]    |

---

## 💡 Tips & Notes

- You can use the Grafana Cloud's **“Explore”** tab to test PromQL queries before using them in dashboards.
- Don't forget to **start containers** before testing cAdvisor metrics.
- Use **panel titles**, units (`%`, `bytes`), and thresholds to improve clarity.
- To identify `instance` label values for `$host`, inspect metrics via **Explore**.

---

