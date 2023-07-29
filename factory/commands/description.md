- List linux services - https://www.tecmint.com/list-all-running-services-under-systemd-in-linux/

  - for listing services and their states:
    systemctl list-units --type=service
    systemctl list-units --type=service --state=active
    systemctl list-units --type=service --state=running
    &^ for cases where system has not been booted with systemd(
    Error: System has not been booted with systemd as init system (PID 1). Can't operate.Failed to connect to bus: Host is down
    ) -> need to find other commands for cases like that
  - get the port of the service:
    netstat -ltup | grep <service-name>
  - list services or port that have been opened in the firewall
    firewall-cmd --list-services [FirewallD]
    firewall-cmd --list-ports

- List windows services - https://www.techtarget.com/searchenterprisedesktop/photostory/4500257331/Top-Windows-command-line-commands/5/Query-the-status-of-services-with-sc-query-state-all

  https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/sc-query

  - for listing services and their states:
    sc query state= all
    sc query <service_name>
    sc \\computername stop service_name
    sc \\computername start service_name

  https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-service?view=powershell-7.3

  Get-Service
  Get-Service "wmi*"
  Get-Service -Displayname "*network*"
  Get-Service -Name "win*" -Exclude "WinRM"
  Get-Service | Where-Object {$\_.Status -eq "Running"}
  Get-Service | Get-Member
    <!-- 
    Get-Service |
  Where-Object {$_.DependentServices} |
    Format-List -Property Name, DependentServices, @{
      Label="NoOfDependentServices"; Expression={$_.dependentservices.count}
    }
    -->

  Get-Service "s\*" | Sort-Object status
  Get-Service "WinRM" -RequiredServices
  "WinRM" | Get-Service
