from enum import Enum

class Windows(Enum):
    
    SERVICES = [
        ('get all services', '--get a list of all service', 'Get-Service'),
        ('get service', '--get a specific service; Arguments: --<Service Name>; Allows only single service name per command', 'Get-Service "--ARGS"'),
        ('get services sorted by status', '--get services sorted by status', 'Get-Service | Sort-Object status'),
        ('get services with status', '--get services with specific status, Arguments: --<status>; Allows single status to be passed', 'Get-Service | Where-Object {$\_.Status -eq "--ARGS"}'),
        ('get non-default windows services', '--get a list of non-default windows services', 'Get-WmiObject win32*service | where { $*.Caption -notmatch "Windows" -and $_.PathName -notmatch "Windows" -and $_.PathName -notmatch "policyhost.exe" -and $_.Name -ne "LSM" -and $_.PathName -notmatch "OSE.EXE" -and $_.PathName -notmatch "OSPPSVC.EXE" -and $_.PathName -notmatch "Microsoft Security Client" }')
    ]
    SYSTEM_RESOURCES = [
        ('get resources', '--get list of counter sets', 'Get-Counter -ListSet \*'),
        ('get memory', '--get a list of memory counters', 'Get-Counter \'\Memory\Available MBytes\''),
        ('get cpu', '--get cpu load percentage', 'Get-WmiObject Win32_Processor | Select LoadPercentage | Format-List'),
        ('get cpu average', '--get cpu load percantage average', 'Get-WmiObject Win32_Processor | Measure-Object -Property LoadPercentage -Average | Select Average')
    ]
    PROCESSES = [
        ('get processes', '--get a list of all active process', 'Get-Process'),
        ('list processes by priority', '--format process by priority', 'Get-Process | Format-Table -View priority'),
        ('show process owner', '--find the process owner', 'Get-Process pwsh -IncludeUserName')
    ]
    NETWORK = [
        ('get network configs', '--get network configurations', 'Get-NetIPConfiguration')
    ]
