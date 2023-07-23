* List linux services - https://www.tecmint.com/list-all-running-services-under-systemd-in-linux/
    - for listing services and their states:
        systemctl list-units --type=service
        systemctl list-units --type=service --state=active
        systemctl list-units --type=service --state=running
    - get the port of the service:
        netstat -ltup | grep <service-name>
    - list services or port that have been opened in the firewall
        firewall-cmd --list-services   [FirewallD]
        firewall-cmd --list-ports
