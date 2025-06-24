from prometheus_client import start_http_server, Gauge
import time
import pwd
import subprocess
import socket

# Get hostname
hostname = socket.gethostname()

# Prometheus metrics with hostname label
LOGGED_IN_USERS = Gauge('logged_in_users', 'Number of users currently logged in', ['hostname'])
TOTAL_USERS = Gauge('total_users', 'Total number of user accounts on the system', ['hostname'])

def get_logged_in_users():
    try:
        output = subprocess.check_output(['who'], text=True)
        users = set(line.split()[0] for line in output.strip().split('\n') if line)
        return len(users)
    except Exception:
        return 0

def get_total_users():
    try:
        return len(pwd.getpwall())
    except Exception:
        return 0

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        LOGGED_IN_USERS.labels(hostname=hostname).set(get_logged_in_users())
        TOTAL_USERS.labels(hostname=hostname).set(get_total_users())
        time.sleep(10)