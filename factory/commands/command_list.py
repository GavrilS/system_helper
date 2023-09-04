from enum import Enum

class Windows(Enum):
    
    SERVICES = [
        ('get all services', '--get a list of all service', 'powershell Get-Service'),
        ('get service', '--get a specific service; Arguments: --<Service Name>; Allows only single service name per command', 'powershell Get-Service "--ARGS"'),
        ('get services sorted by status', '--get services sorted by status', 'powershell Get-Service | Sort-Object status'),
        ('get services with status', '--get services with specific status, Arguments: --<status>; Allows single status to be passed', 'powershell Get-Service | Where-Object {$\_.Status -eq "--ARGS"}'),
        ('get non-default windows services', '--get a list of non-default windows services', 'powershell Get-WmiObject win32*service | where { $*.Caption -notmatch "Windows" -and $_.PathName -notmatch "Windows" -and $_.PathName -notmatch "policyhost.exe" -and $_.Name -ne "LSM" -and $_.PathName -notmatch "OSE.EXE" -and $_.PathName -notmatch "OSPPSVC.EXE" -and $_.PathName -notmatch "Microsoft Security Client" }')
    ]
    SYSTEM_RESOURCES = [
        ('get resources', '--get list of counter sets', 'powershell Get-Counter -ListSet \*'),
        ('get memory', '--get a list of memory counters', 'powershell Get-Counter \'\Memory\Available MBytes\''),
        ('get cpu', '--get cpu load percentage', 'powershell Get-WmiObject Win32_Processor | Select LoadPercentage | Format-List'),
        ('get cpu average', '--get cpu load percantage average', 'powershell Get-WmiObject Win32_Processor | Measure-Object -Property LoadPercentage -Average | Select Average')
    ]
    PROCESSES = [
        ('get processes', '--get a list of all active process', 'powershell Get-Process'),
        ('list processes by priority', '--format process by priority', 'powershell Get-Process | Format-Table -View priority'),
        ('show process owner', '--find the process owner', 'powershell Get-Process pwsh -IncludeUserName')
    ]
    NETWORK = [
        ('get network configs', '--get network configurations', 'powershell Get-NetIPConfiguration')
    ]
