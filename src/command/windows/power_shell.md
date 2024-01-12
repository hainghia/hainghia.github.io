## Check Ram Windows

```shell
wmic memorychip get devicelocator, manufacturer
wmic memorychip get devicelocator, partnumber
wmic memorychip get devicelocator, serialnumber
wmic memorychip get banklabel, serialnumber
wmic memorychip get devicelocator, capacity
wmic memorychip get devicelocator, speed
wmic memorychip get devicelocator, memorytype
```

## [Installing Chocolatey](https://docs.chocolatey.org/en-us/choco/setup)

```shell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

```shell
choco upgrade chocolatey
```
