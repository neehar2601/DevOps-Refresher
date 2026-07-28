1. Real-Time Service Control

To change the state of a service on your currently running system, use start, stop, or restart, run the following command:


$ sudo systemctl start apache2

$ sudo systemctl stop apache2

$ sudo systemctl restart apache2
2. Boot-Time Configuration

To determine whether a service should launch automatically when the computer turns on, use enable or disable:


$ sudo systemctl enable apache2

$ sudo systemctl disable apache2
3. Monitoring Service Health

To check if a service is running, view its recent logs, or see its process ID (PID), use the status command:


$ sudo systemctl status apache2