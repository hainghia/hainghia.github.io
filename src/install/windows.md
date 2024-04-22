# Install Windows

## [Installing Chocolatey](https://docs.chocolatey.org/en-us/choco/setup)

*Install with PowerShell.exe (Administrators)*

```shell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

```shell
choco upgrade chocolatey
```

## [Install OpenSSH for Windows](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell)
```shell
(New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
```
```shell
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```
*Then, install the server or client components as needed:*
```shell
# Install the OpenSSH Client
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```
*To start and configure OpenSSH Server for initial use, open an elevated PowerShell prompt (right click, Run as an administrator), then run the following commands to start the sshd service:*
```shell
# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}
```

### Connect to OpenSSH Server
Then, install the server or client components as needed:
```shell
ssh domain\username@servername
```

## [Download file by Wget](https://www.gnu.org/software/wget/manual/wget.html)
```shell
wget -r --tries=10 https://fly.srk.fer.hr/ -o log
```

## [Installing Ansible on Windows](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
> You cannot use a Windows system for the Ansible control node. See Can Ansible run on Windows? To install Ansible on WSL, the following commands can be run in the bash terminal:
```shell
sudo apt-get install software-properties-common
sudo apt-get install gnupg
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install python3-pip git libffi-dev libssl-dev -y
pip install --user ansible pywinrm

export PATH=$PATH:$HOME/.local/bin
source ~/.bashrc

sudo apt install ansible
```
*If you encounter timeout errors when running Ansible on the WSL, this may be due to an issue with sleep not returning correctly. The following workaround may resolve the issue:*
```shell
mv /usr/bin/sleep /usr/bin/sleep.orig
ln -s /bin/true /usr/bin/sleep
```
### Ansible command shell autocompletion
```shell
pip --version
pip install pipx
which pipx

pip3 install argcomplete
#python3 -m pip install --user argcomplete

activate-global-python-argcomplete --user

source ~/.profile
source ~/.bashrc
```