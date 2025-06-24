# Kubernetes Monitoring Dashboard (k3s)

**Skills**: K3s, kube-prometheus-stack, Grafana, Helm, Kubernetes Monitoring

**Overview**:
This project guides you through setting up a monitoring dashboard for a single-node K3s Kubernetes cluster using the kube-prometheus-stack and Grafana. You'll gain hands-on experience with cluster monitoring, metric collection, and dashboard creation.

**Tasks**:

1. **Set up a Single-node K3s Cluster**
  - Install K3s on a Linux VM or cloud instance.
  - Verify cluster status with `kubectl get nodes`.

2. **Install kube-prometheus-stack using Helm**
  - Add the Prometheus Community Helm repo:
    ```sh
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update
    ```
  - Install the stack:
    ```sh
    helm install monitoring prometheus-community/kube-prometheus-stack
    ```

3. **Enable `kube-state-metrics`**
  - Ensure `kube-state-metrics` is enabled in the Helm values or via:
    ```sh
    helm upgrade monitoring prometheus-community/kube-prometheus-stack --set kubeStateMetrics.enabled=true
    ```

4. **Access Grafana**
  - Forward the Grafana service port:
    ```sh
    kubectl port-forward svc/monitoring-grafana 3000:80
    ```
  - Login with default credentials (`admin/prom-operator`).

5. **Create Dashboards in Grafana**
  - **Pod Health**: Visualize pod status, restarts, and failures.
  - **Node Resource Usage**: Display CPU, memory, and disk usage per node.
  - **Deployment Status**: Track deployment rollouts and replica counts.
  - Import community dashboards or build custom panels using Prometheus queries.

**Deliverables**:
- Screenshots of Grafana dashboards.
- A brief write-up on key metrics and alerts configured.

**Bonus**:
- Set up alerting rules for critical events (e.g., node down, pod crashloop).
- Explore multi-node K3s monitoring.
