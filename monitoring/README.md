# Monitoring with Grafana Cloud

## Introduction

Monitoring is essential to ensure your applications and infrastructure are healthy, performant, and secure. Grafana Cloud provides a powerful, managed platform for monitoring metrics, logs, and traces.

---

## Why Do We Need Monitoring?

- **Detect Anomalies:** Identify abnormal behavior in applications and infrastructure.
- **Error & Exception Tracking:** Monitor errors and exceptions to improve robustness.
- **Production Readiness:** Ensure stable environments and early bug detection.
- **Proactive Actions:** Enable prompt responses to incidents and future events.

---

## What to Monitor?

- **System Metrics:** CPU, Memory, Storage, IO, Network
- **Logs:** Exceptions, Errors, Critical Events
- **Security Events:** Login attempts, Unknown IPs, Phishing, Mining, Unwanted Software, Privilege Escalation, DDoS, Brute Force
- **Application Telemetry:** Thread counts, API calls (status codes), Usage trends, Request queues, Regional availability, SSL status
- **Website Monitoring:** Synthetic checks for uptime and performance

---

## Monitoring Types

- **System Monitoring:** Track server and infrastructure health.
- **Synthetic Monitoring:** Simulate user interactions to test website availability.
- **Application Monitoring:** Observe application-level metrics and logs.

---

## Grafana Cloud Overview

Grafana Cloud is a fully managed observability platform that integrates:

- **Grafana:** Visualization and dashboarding
- **Prometheus:** Metrics collection and querying
- **Loki:** Log aggregation and querying
- **Tempo:** Distributed tracing

---

## Getting Started with Grafana Cloud

1. **Sign Up for Grafana Cloud**
    - Visit [Grafana Cloud](https://grafana.com/products/cloud/) and create a free account.

2. **Create a Stack**
    - Set up a new stack for your project/environment.

3. **Obtain API Tokens**
    - Generate API tokens for metrics, logs, and traces ingestion.

4. **Install Monitoring Agents**
    - **Prometheus Agent:** For system and application metrics.
    - **Loki Agent:** For log collection.
    - **Synthetic Monitoring:** Configure synthetic checks via the Grafana Cloud UI.

5. **Configure Data Sources in Grafana**
    - Add Prometheus and Loki as data sources in your Grafana Cloud instance.

6. **Build Dashboards**
    - Use pre-built dashboards or create custom ones to visualize your data.

7. **Set Up Alerts**
    - Configure alerting rules for critical metrics and logs.

---

## Example: System Monitoring Setup

1. **Install Prometheus Agent**
    ```sh
    curl -fsSL https://raw.githubusercontent.com/grafana/agent/release/production/install.sh | sh
    ```
    - Configure the agent with your Grafana Cloud credentials.

2. **Install Loki Agent**
    - Follow [Loki Agent documentation](https://grafana.com/docs/loki/latest/clients/promtail/).

3. **Verify Data Ingestion**
    - Check Grafana dashboards for incoming metrics and logs.

---

## Creating a Custom Prometheus Exporter

Custom exporters allow you to expose application-specific metrics to Prometheus. Here’s a simple example using Python and the [`prometheus_client`](https://github.com/prometheus/client_python) library:

1. **Install the Prometheus client library:**
    ```sh
    pip install prometheus_client
    ```

2. **Create a simple exporter:**
    ```python
    from prometheus_client import start_http_server, Gauge
    import random
    import time

    # Create a metric to track
    my_metric = Gauge('my_custom_metric', 'An example custom metric')

    if __name__ == '__main__':
        start_http_server(8000)
        while True:
            my_metric.set(random.random())
            time.sleep(5)
    ```

3. **Run your exporter:**
    ```sh
    python exporter.py
    ```

4. **Configure Prometheus Agent to scrape your exporter:**
    Add a scrape config in your Prometheus Agent configuration:
    ```yaml
    scrape_configs:
      - job_name: 'custom_exporter'
        static_configs:
          - targets: ['localhost:8000']
    ```

5. **Visualize in Grafana:**
    - After data is ingested, build dashboards in Grafana Cloud to visualize your custom metrics.

---

## Useful Resources

- [Grafana Cloud Documentation](https://grafana.com/docs/grafana-cloud/)
- [Prometheus Agent Setup](https://grafana.com/docs/agent/latest/)
- [Loki Log Collection](https://grafana.com/docs/loki/latest/)
- [Synthetic Monitoring](https://grafana.com/docs/grafana-cloud/synthetic-monitoring/)
- [Prometheus Exporter Best Practices](https://prometheus.io/docs/instrumenting/writing_exporters/)

---

## Summary

Grafana Cloud simplifies monitoring by providing a unified platform for metrics, logs, and traces. You can monitor standard system metrics and also create custom Prometheus exporters to track application-specific data. Follow the steps above to get started and ensure your systems are observable and reliable.

