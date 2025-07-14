


#  **Docker Fundamentals Notes**



## **Introduction to Docker**

* **Docker** is a platform used to develop, ship, and run applications inside containers.
* Containers are lightweight, portable, and run consistently across different environments.

### Why Docker?

* Eliminates "It works on my machine" issues.
* Fast startup and low overhead.
* Easy scaling and orchestration.

---

## **Key Concepts**

### **Images**

* Read-only templates used to create containers.
* Built from a Dockerfile.
* Examples: `ubuntu`, `nginx`, `node`, etc.

## **. Docker Architecture vs VM Architecture**

###  **Docker Architecture Diagram (Descriptive)**

```
+--------------------------------------------------------+
|                    Host Operating System               |
| +-------------------+    +---------------------------+ |
| |   Docker Engine   |    |       VirtualBox/VMware   | |
| |-------------------|    |---------------------------| |
| |  Docker CLI       |    |  Hypervisor               | |
| |  Docker Daemon    |    |  Guest OS (Linux/Windows) | |
| |  Container Runtime|    |  App A, B, C               | |
| +-------------------+    +---------------------------+ |
|     Container A, B, C      (VMs with full OS inside)   |
+--------------------------------------------------------+
```

---

## **. Why Docker Instead of Virtual Machines (VMs)?**

### **Docker vs Virtual Machines**

| Feature                 | Docker Containers                        | Virtual Machines (VMs)                    |
| ----------------------- | ---------------------------------------- | ----------------------------------------- |
| **Virtualization Type** | OS-level (container)                     | Hardware-level (hypervisor)               |
| **Startup Time**        | Seconds                                  | Minutes                                   |
| **Footprint**           | Lightweight (shares host OS kernel)      | Heavy (includes full OS per VM)           |
| **Performance**         | Near-native                              | Slower due to full OS layer               |
| **Resource Usage**      | Minimal                                  | High (RAM, CPU for each OS)               |
| **Isolation**           | Process-level isolation                  | Full OS isolation                         |
| **Portability**         | High (runs anywhere Docker is supported) | Lower (requires compatible hypervisor/OS) |

---

### **Containers**

* Running instances of Docker images.
* Ephemeral (short-lived by default), but can persist data with volumes.

### **Dockerfile**

* Script of instructions to build a Docker image.
* Example:

  ```dockerfile
  FROM python:3.9
  COPY . /app
  WORKDIR /app
  RUN pip install -r requirements.txt
  CMD ["python", "app.py"]
  ```

### **Volumes**

* Used for persistent storage.
* Mounted to a container from host.

### **Docker Hub**

* Public registry of Docker images.
* Can also use private registries.

---

## **Installing Docker**

* Available on Linux, macOS, Windows.
* Check installation with:

  ```bash
  docker --version
  docker info
  ```

---

## **Basic Docker Commands**

### **Image Commands**

```bash
docker pull <image-name>            # Pull image from Docker Hub
docker images                       # List images
docker rmi <image-id>               # Remove image
```

### **Container Commands**

```bash
docker run <image>                      # Run container
docker run -d -p 80:80 nginx            # Detached mode with port mapping
docker ps                               # List running containers
docker ps -a                            # All containers
docker stop <container-id>             # Stop container
docker rm <container-id>               # Remove container
```

### **Building Images**

```bash
docker build -t myapp .                # Build image from Dockerfile
```

---

## **Docker Networking**

* **Bridge** (default): Containers communicate on the same host.
* **Host**: Shares host network stack.
* **None**: No network.
* Create custom networks:

  ```bash
  docker network create mynetwork
  docker network ls
  ```

---

## **Docker Compose**

* Tool for defining and running multi-container Docker apps using `docker-compose.yml`.

### Example:

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "80:80"
  app:
    build: .
    volumes:
      - .:/app
    depends_on:
      - web
```

### Commands:

```bash
docker-compose up                    # Start services
docker-compose down                  # Stop and remove services
```

---

## **Docker Volumes**

* Used to persist and share data.

```bash
docker volume create myvolume
docker run -v myvolume:/data ubuntu
docker volume ls
```

---

## **Dockerfile Instructions (Common)**

| Instruction | Description                                        |
| ----------- | -------------------------------------------------- |
| `FROM`      | Base image                                         |
| `COPY`      | Copy files from host                               |
| `ADD`       | Like COPY but supports remote URLs and auto-unpack |
| `WORKDIR`   | Set working directory                              |
| `RUN`       | Execute commands while building                    |
| `CMD`       | Default command                                    |
| `EXPOSE`    | Informational; expose port                         |
| `ENV`       | Set environment variable                           |

---

## **Docker Best Practices**

* Keep images small (use slim/base images).
* Use multi-stage builds.
* Avoid hardcoding secrets in images.
* Tag images properly.
* Clean up unused images, volumes, and containers.

---

## **Docker vs Virtual Machines**

| Docker Containers   | Virtual Machines      |
| ------------------- | --------------------- |
| Lightweight         | Heavy (includes OS)   |
| Faster startup      | Slower boot time      |
| Shares OS kernel    | Runs full OS instance |
| Less resource usage | More resource usage   |

---

## **Troubleshooting Commands**

```bash
docker logs <container-id>              # View container logs
docker exec -it <container-id> bash     # Access container shell
docker inspect <container-id>           # Detailed info
docker stats                            # Resource usage
```

---





### **Why Use Docker Instead of VMs?**

* **Faster Development Cycle**: Start containers in seconds.
* **Efficiency**: Uses system resources more effectively.
* **Consistency Across Environments**: Works the same on any system.
* **Simplified CI/CD**: Easily integrates into pipelines.
* **Microservices Friendly**: Perfect for splitting apps into small, manageable services.
* **Scalability**: Ideal for cloud-native and Kubernetes-based deployments.

---



###  Key Docker Components:

* **Docker CLI**: Command-line interface.
* **Docker Daemon**: Background service managing containers.
* **Container Runtime**: Executes containers.
* **Images & Containers**: Built from Dockerfiles and run in isolated environments.

---
