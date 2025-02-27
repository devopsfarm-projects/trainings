### Shell Script
```sh
#!/bin/bash

network="192.168.1.0/24"  # Change this to match your network range
output_file="network_scan_results.txt"

echo "Scanning network: $network" > "$output_file"

# Find all live hosts
for ip in $(seq 1 254); do
    ping -c 1 -W 1 192.168.1.$ip &>/dev/null && echo "192.168.1.$ip is up" | tee -a "$output_file"
done

# Scan for open ports using netcat
for ip in $(grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' "$output_file"); do
    echo "Scanning ports on $ip..." | tee -a "$output_file"
    for port in $(seq 1 1024); do  # Scanning all common ports
        nc -zv $ip $port &>/dev/null && echo "Port $port open on $ip" | tee -a "$output_file"
    done
done

echo "Scan complete. Results saved in $output_file."
```


### Explaination
The shell script is scanning the network for live hosts by pinging each IP in the subnet. Here’s a detailed explanation of how it works:

### **Script Breakdown**
```sh
#!/bin/bash
```
- This is a shebang (`#!`) that tells the system to use the `bash` shell to interpret the script.

```sh
network="192.168.1.0/24"  # Change this to match your network range
output_file="network_scan_results.txt"
```
- Defines the target network range (`192.168.1.0/24`), meaning all IPs from `192.168.1.1` to `192.168.1.254`.
- Specifies the output file where results will be stored.

```sh
echo "Scanning network: $network" > "$output_file"
```
- Prints a message indicating the scan has started and writes it to the output file.

```sh
for ip in $(seq 1 254); do
    ping -c 1 -W 1 192.168.1.$ip &>/dev/null && echo "192.168.1.$ip is up" | tee -a "$output_file"
done
```
- A loop iterates through IPs from `.1` to `.254`.
- `ping -c 1 -W 1 192.168.1.$ip &>/dev/null`
  - `-c 1`: Sends a single ICMP echo request.
  - `-W 1`: Waits 1 second for a response.
  - `&>/dev/null`: Suppresses output to avoid cluttering the terminal.
- If the host responds, the IP is printed and saved to the output file using `tee -a`.

```sh
echo "Scan complete. Results saved in $output_file."
```
- Displays a completion message.

### **Possible Enhancements**
1. **Scan Common Ports**
   - Use `nc` (Netcat) or `nmap` to check for open ports.
   ```sh
   for ip in $(cat network_scan_results.txt | awk '{print $1}'); do
       for port in 22 80 443 3389; do  # Common ports: SSH, HTTP, HTTPS, RDP
           nc -zv $ip $port 2>&1 | tee -a "$output_file"
       done
   done
   ```
2. **Use `curl` and `wget` to check web services**
   ```sh
   for ip in $(cat network_scan_results.txt | awk '{print $1}'); do
       curl -Is http://$ip | head -n 1 | tee -a "$output_file"
       wget --spider http://$ip &>> "$output_file"
   done
   ```