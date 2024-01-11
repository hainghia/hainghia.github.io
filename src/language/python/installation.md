# [Installation](https://www.python.org/downloads/)
### [Installation Python](https://www.python.org/downloads/)

*Download the latest version for macOS*

- Step 1: https://www.python.org/downloads/
- Step 2: Add the following line to `~/.zshrc`

```bash
export PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin:$PATH"
export PATH="/Library/Frameworks/Python.framework/Versions/3.12/bin/pip3.12:$PATH"
alias python='python3.12'
alias pip='pip3.12'
```

### [Installation Pip](https://pip.pypa.io/en/stable/installation/)
```shell
python3 -m pip install --upgrade pip
```

### [Pip Configuration](https://pip.pypa.io/en/stable/topics/configuration/#configuration)

```shell
mkdir ~/.config/pip
touch ~/.config/pip/pip.conf
echo '[global]' >> ~/.config/pip/pip.conf
echo 'break-system-packages = true' >> ~/.config/pip/pip.conf
```


## Command line
```shell
where python3
pip list
pip freeze > requirements.txt
```