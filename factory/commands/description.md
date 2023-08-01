### Service commands

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

  ~ Get list of non windows default services - https://powershelladministrator.com/2014/04/28/get-all-non-default-windows-services/comment-page-1/

    <!-- #Get all services where its caption or its pathname doesn't contain Windows -->

  Get-WmiObject win32*service | where { $*.Caption -notmatch "Windows" -and $\_.PathName -notmatch "Windows" }
    <!-- #Adding exclusion for "policyhost.exe" removes Microsoft Policy Platform service -->

  Get-WmiObject win32*service | where { $*.Caption -notmatch "Windows" -and $_.PathName -notmatch "Windows" -and $_.PathName -notmatch "policyhost.exe" }

    <!-- #Adding exclusion for service name "LSM" removes the Local Session Manager service -->

  Get-WmiObject win32*service | where { $*.Caption -notmatch "Windows" -and $_.PathName -notmatch "Windows" -and $_.PathName -notmatch "policyhost.exe" -and $\_.Name -ne "LSM" }

    <!-- #Adding exclusion for "OSE.EXE" removes the Office Source Engine Service -->

  Get-WmiObject win32*service | where { $*.Caption -notmatch "Windows" -and $_.PathName -notmatch "Windows" -and $_.PathName -notmatch "policyhost.exe" -and $_.Name -ne "LSM" -and $_.PathName -notmatch "OSE.EXE" }

    <!-- #Adding exclusion for "OSPPSVC.EXE" removes the Office Software Protection Platform Service -->

  Get-WmiObject win32*service | where { $*.Caption -notmatch "Windows" -and $_.PathName -notmatch "Windows" -and $_.PathName -notmatch "policyhost.exe" -and $_.Name -ne "LSM" -and $_.PathName -notmatch "OSE.EXE" -and $\_.PathName -notmatch "OSPPSVC.EXE" }

  <!-- #Adding exclusion for "Microsoft Security Client" removes Microsoft Security Client (SCEP)
  #This leaves us with all non-default services on a Windows 2012 R2 server! -->

  $NonDefaultServices = Get-WmiObject win32*service | where { $*.Caption -notmatch "Windows" -and $_.PathName -notmatch "Windows" -and $_.PathName -notmatch "policyhost.exe" -and $_.Name -ne "LSM" -and $_.PathName -notmatch "OSE.EXE" -and $_.PathName -notmatch "OSPPSVC.EXE" -and $_.PathName -notmatch "Microsoft Security Client" }

  $NonDefaultServices.DisplayName # Service Display Name (full name)
  $NonDefaultServices.PathName # Service Executable
  $NonDefaultServices.StartMode # Service Startup mode
  $NonDefaultServices.StartName # Service RunAs Account
  $NonDefaultServices.State # Service State (running/stopped etc)
  $NonDefaultServices.Status # Service Status
  $NonDefaultServices.Started # Service Started status
  $NonDefaultServices.Description # Service Description

### System resources command

https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-counter?view=powershell-7.3

  <!-- Get-Counter uses the ListSet parameter with an asterisk (*) to get the list of counter sets. The dot (.) in the MachineName column represents the local computer -->

Get-Counter -ListSet \*

  <!-- Get-Counter uses the Counter parameter to specify the counter path \Processor(_Total)\% Processor Time. The SampleInterval parameter sets a two-second interval to check the counter. MaxSamples determines that three is the maximum number of times to check the counter. -->

Get-Counter -Counter "\Processor(\_Total)\% Processor Time" -SampleInterval 2 -MaxSamples 3

  <!-- Get-Counter uses the Counter parameter to specify the \Processor\% Processor Time counter. The Continuous parameter specifies to get samples every second until the command is stopped with CTRL+C. -->

Get-Counter -Counter "\Processor(\_Total)\% Processor Time" -Continuous

  <!-- This example uses the pipeline to get the counter list set and then sort the list in alphabetical order. -->
  <!-- Get-Counter -ListSet * |
  Sort-Object -Property CounterSetName |
    Format-Table CounterSetName, CounterSetType -AutoSize -->

  <!-- In this example, Start-Job runs a Get-Counter command as a background job on the local computer. To view the performance counter output from the job, use the Receive-Job cmdlet. -->

Start-Job -ScriptBlock {Get-Counter -Counter "\LogicalDisk(\_Total)\% Free Space" -MaxSamples 1000}

  <!-- This example uses a variable to get performance counter data from two computers. -->

$DiskReads = "\LogicalDisk(C:)\Disk Reads/sec"
$DiskReads | Get-Counter -ComputerName Server01, Server02 -MaxSamples 10

  <!-- In this example, a single value is returned for each performance counter in the local computer's Memory counter set. -->

$MemCounters = (Get-Counter -ListSet Memory).Paths
Get-Counter -Counter $MemCounters

  <!-- Get a list of memory counters -->

Get-Counter '\Memory\Available MBytes'
Get-Counter '\Processor(\_Total)\% Processor Time'
Get-Counter -ListSet _memory_ | Select-Object -ExpandProperty Counter

  <!-- CPU load. -->

Get-WmiObject Win32_Processor | Select LoadPercentage | Format-List
Get-WmiObject Win32_Processor | Measure-Object -Property LoadPercentage -Average | Select Average

  <!-- Script format -->
  <!-- $totalRam = (Get-CimInstance Win32_PhysicalMemory | Measure-Object -Property capacity -Sum).Sum
while($true) {
    $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $cpuTime = (Get-Counter '\Processor(_Total)\% Processor Time').CounterSamples.CookedValue
    $availMem = (Get-Counter '\Memory\Available MBytes').CounterSamples.CookedValue
    $date + ' > CPU: ' + $cpuTime.ToString("#,0.000") + '%, Avail. Mem.: ' + $availMem.ToString("N0") + 'MB (' + (104857600 * $availMem / $totalRam).ToString("#,0.0") + '%)'
    Start-Sleep -s 2
} -->

### System processes commands:

<!-- This command gets a list of all active processes running on the local computer -->

Get-Process

<!-- Get available data per process -->

Get-Process winword, explorer | Format-List \*

  <!-- List processes with priority -->

$A = Get-Process
$A | Get-Process | Format-Table -View priority

  <!-- Find the owner -->

Get-Process pwsh -IncludeUserName

### Network configurations

<!-- The Get-NetIPConfiguration cmdlet gets network configuration, including usable interfaces, IP addresses, and DNS servers.

If you do not specify any parameters, this cmdlet gets IP configuration properties for all non-virtual connected interfaces on a computer. -->

Get-NetIPConfiguration

Get-NetIPConfiguration -All

Get-NetIPConfiguration -Verbose
