# Networking Commands, Protocols, and IP Basics in Linux

## 1. Networking Commands in Linux

### Checking Network Interfaces

```sh
ip a  # Shows all network interfaces and IP addresses
ifconfig  # (Deprecated) Displays network interfaces
nmcli dev status  # Displays network device status (for NetworkManager-based systems)
```

### Managing IP Addresses and Routes

```sh
ip addr show  # Lists assigned IP addresses
ip route show  # Displays the routing table
ip link set eth0 up/down  # Enable/disable a network interface
```

### Testing Connectivity

```sh
ping <destination>  # Checks if a remote host is reachable
traceroute <destination>  # Traces the path packets take
mtr <destination>  # A continuous traceroute with statistics
curl -I <url>  # Fetch headers of a URL
wget --spider <url>  # Checks if a URL is reachable
```

### DNS and Name Resolution

```sh
nslookup <domain>  # Queries DNS records
dig <domain>  # More detailed DNS lookup
host <domain>  # Resolves a domain to an IP
```

### Network Services and Ports

```sh
netstat -tulnp  # Lists open ports and listening services
ss -tulnp  # Modern alternative to netstat
lsof -i :<port>  # Checks which process is using a specific port
```

### Network Troubleshooting

```sh
arp -a  # Shows the ARP cache
tcpdump -i eth0  # Captures network packets
nc -zv <host> <port>  # Checks if a port is open on a remote host
```

### Firewall Management

```sh
iptables -L  # Lists firewall rules
firewalld --list-all  # Shows firewall rules (for firewalld systems)
ufw status  # Checks firewall status (for UFW systems)
```

## 2. Protocols and Ports

| Protocol | Description                         | Port     |
| -------- | ----------------------------------- | -------- |
| HTTP     | Web traffic (unencrypted)           | 80       |
| HTTPS    | Secure web traffic                  | 443      |
| FTP      | File Transfer Protocol              | 21       |
| SSH      | Secure Shell (remote login)         | 22       |
| Telnet   | Remote login (insecure)             | 23       |
| SMTP     | Sending emails                      | 25       |
| DNS      | Domain Name System                  | 53       |
| DHCP     | Dynamic Host Configuration Protocol | 67, 68   |
| POP3     | Email retrieval                     | 110      |
| IMAP     | Email access                        | 143      |
| LDAP     | Directory access                    | 389      |
| RDP      | Remote Desktop Protocol             | 3389     |
| SNMP     | Simple Network Management Protocol  | 161, 162 |

## 3. IP Addressing

### Types of IP Addresses

1. **IPv4** – 32-bit address (e.g., `192.168.1.1`)
2. **IPv6** – 128-bit address (e.g., `2001:db8::ff00:42:8329`)

### IP Address Classes (IPv4)

| Class | Start Address | End Address     | Default Subnet Mask | Usage           |
| ----- | ------------- | --------------- | ------------------- | --------------- |
| **A** | 1.0.0.0       | 126.255.255.255 | 255.0.0.0           | Large networks  |
| **B** | 128.0.0.0     | 191.255.255.255 | 255.255.0.0         | Medium networks |
| **C** | 192.0.0.0     | 223.255.255.255 | 255.255.255.0       | Small networks  |
| **D** | 224.0.0.0     | 239.255.255.255 | N/A                 | Multicasting    |
| **E** | 240.0.0.0     | 255.255.255.255 | N/A                 | Reserved        |

### Private IP Ranges

| Address Range                 | Class |
| ----------------------------- | ----- |
| 10.0.0.0 – 10.255.255.255     | A     |
| 172.16.0.0 – 172.31.255.255   | B     |
| 192.168.0.0 – 192.168.255.255 | C     |

## 4. CIDR Notation (Classless Inter-Domain Routing)

CIDR allows more efficient use of IP addresses by defining subnets.

### Subnet Masks & CIDR

| CIDR | Subnet Mask     | Total IPs  | Usable IPs |
| ---- | --------------- | ---------- | ---------- |
| /8   | 255.0.0.0       | 16,777,216 | 16,777,214 |
| /16  | 255.255.0.0     | 65,536     | 65,534     |
| /24  | 255.255.255.0   | 256        | 254        |
| /30  | 255.255.255.252 | 4          | 2          |

### Example CIDR Calculation

- `192.168.1.0/24` → **Subnet Mask:** `255.255.255.0`, **IPs:** 256 (usable: 254)
- `10.0.0.0/16` → **Subnet Mask:** `255.255.0.0`, **IPs:** 65,536 (usable: 65,534)

## 5. Assignment: 
See [problem.md](./assignments/2/problem.md)