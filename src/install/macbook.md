# Install MacOS

## [Homebrew](https://brew.sh/)

```shell
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Then Installation successful

```shell
(echo; echo 'eval "$(/opt/homebrew/bin/brew shellenv)"') >> /Users/hainghia/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

```shell
brew --version
rm -rf $(brew --prefix)/var/homebrew/locks
brew cleanup
brew doctor
brew missing
```

## [ZSH](https://ohmyz.sh/)

https://sourabhbajaj.com/mac-setup/iTerm/zsh.html

```shell
brew install zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

### ZSH Manager

```shell
zsh --version
chsh -s $(which zsh) # Đặt ZSH là Shell mặc định
source ~/.zshrc # Khi cấu hình Zsh xong cần khởi động lại Shell
```

### [Theme Zsh: Muse](https://github.com/ohmyzsh/ohmyzsh/wiki/Themes#muse)

```shell
vim .zshrc
```

```shell
# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="robbyrussell"
```

## [jq is a lightweight and flexible command-line JSON processor](https://jqlang.github.io/jq/download/)

```shell
brew install jq
```

## [TREE: Displays the directory tree structure of Repositories](https://github.com/Old-Man-Programmer/tree)

```shell
brew install tree
```

### Displays the directory tree structure of Repositories With GIT

```shell
git config --global alias.tree '! git ls-tree --full-name --name-only -t -r HEAD | sed -e "s/[^-][^\/]*\//   |/g" -e "s/|\([^ ]\)/|-- \1/"'
```

```shell
git tree
```

## [Amazon CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/command-line.html)

```shell
# Download file
https://desktop-release.codewhisperer.us-east-1.amazonaws.com/latest/CodeWhisperer.dmg
```

## [Auto ssh](https://www.harding.motd.ca/autossh/)

- [brew autossh](https://formulae.brew.sh/formula/autossh#default)
- https://command-not-found.com/autossh
  *Run, monitor and restart SSH connections. Auto-reconnects to keep port forwarding tunnels up.*

```shell
brew install autossh
```

### Use `Forwarding tunnels Redshift`

```shell
autossh -f -M 0 -N -N -o "ServerAliveInterval 10" -o "ServerAliveCountMax 3" -L 5439:host.us-east-1.redshift.amazonaws.com:5439 nghia.ho@34.198.8.139
```

## [LocalStack](https://github.com/localstack/localstack)

```shell
brew install localstack
pip install --upgrade pip
pip install --upgrade setuptools
python3 -m pip install localstack
```

## [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

```shell
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
which aws
aws --version
```

## [Install the Session Manager plugin on macOS](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-macos-overview.html)

**requires either Python ^3.3**

```shell
curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac_arm64/sessionmanager-bundle.zip" -o "sessionmanager-bundle.zip"
unzip sessionmanager-bundle.zip
sudo ./sessionmanager-bundle/install -i /usr/local/sessionmanagerplugin -b /usr/local/bin/session-manager-plugin
./sessionmanager-bundle/install -h
```

### Uninstall the plugin

```shell
sudo rm -rf /usr/local/sessionmanagerplugin
sudo rm /usr/local/bin/session-manager-plugin
```

### [Uninstalling the AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/uninstall.html)

```shell
which aws
ls -l /usr/local/bin/aws
sudo rm /usr/local/bin/aws
sudo rm /usr/local/bin/aws_completer
sudo rm -rf /usr/local/aws-cli
sudo rm -rf ~/.aws/
```

## [Installing the AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)

- [AWS Serverless Application Model (SAM)](https://github.com/aws/aws-sam-cli)
  Tải file `aws-sam-cli-macos-arm64.pkg`  và cài đặt

```
https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-macos-arm64.pkg
```

## `~/.aws/config`

```shell
[default]
region = us-east-1
output = ENTER
cli_pager = cat

[profile permate-root] # -> account này để pull code từ codecommit
sso_session = pm-dev
sso_account_id = 678622957589
sso_role_name = CodeCommitAccess
region = us-east-1
output = json

[profile permate-dev] # -> account này cho môi trường dev
sso_session = pm-dev
sso_account_id = 848671439054
sso_role_name = ReadOnlyAccess
region = us-east-1
output = json

[profile permate-stg] # -> account này cho môi trường dev
sso_session = pm-dev
sso_account_id = 015474994698
sso_role_name = ReadOnlyAccess
region = ap-southeast-1
output = json

[sso-session pm-dev]
sso_region = ap-southeast-1
sso_start_url = https://pm-dev.awsapps.com/start
sso_registration_scopes = sso:account:access
duration_seconds = 43200
```

## [Charles web proxy](https://formulae.brew.sh/cask/charles#default)

> https://www.charlesproxy.com

```shell
brew install --cask charles
```

### License Key

```shell
# License Key 1
Name: NamLee.Net
Key: fcc8357835cd7ef472

# License Key 2
Name: https://zhile.io
Key: 48891cf209c6d32bf4
```

## [SSH](https://www.openssh.com/)

- [GitHub: Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
- [GitLab: Use SSH keys to communicate with GitLab](https://docs.gitlab.com/ee/user/ssh.html)

```shell
ssh-keygen -t ed25519 -C "hohainghia19@gmail.com"
ssh-keygen -o -t rsa -b 4096 -C "hohainghia19@gmail.com"
```

## [GIT](https://git-scm.com/)

```shell
git config --list

```

### Config `cat ~/.gitconfig`

```shell
git config --global user.name "Hai Nghia"
git config --global user.email "hohainghia19@gmail.com"
git config --global core.editor "vim"
git config --system core.longpaths true
git config --global core.fsmonitor true
git config --global core.compression 0
git config --global --add push.autoSetupRemote true
git config --global push.autoSetupRemote true
git config --global url."https://".insteadOf git://
git config --global url."https://github.com".insteadOf git://github.com
```

### reset or revert a file to a specific revision

*If you want to revert to the commit before c5f567, append ~1 (where 1 is the number of commits you want to go back*

```shell
git checkout c5f567~1 -- file1/to/restore file2/to/restore
```

## Using multiple github accounts with ssh keys `.ssh/config`

```shell
Host *
    StrictHostKeyChecking accept-new

Host git-codecommit.*.amazonaws.com
    User APKAZ4AIUSAK7KV5PS7H

# Default github account: hainghia
Host github.com-hainghia
   HostName github.com
   IdentityFile ~/.ssh/id_ed25519
   IdentitiesOnly yes

# Other github account: hohainghia
Host github.com-hohainghia
   HostName github.com
   IdentityFile ~/.ssh/id_rsa
   IdentitiesOnly yes
```

**! Lưu ý: Cần điền chính xác Git hostname ví dụ git@github.com-hainghia hoặc git@github.com-kukun vì url clone mặc định
sẽ bỏ qua Git hostname dẫn đến không mapping được với ssh key tương ứng**

```shell
git clone git@github.com-account1:<account1-username>/<repository-name>.git 
#Not
git clone git@github.com:<account1-username>/<repository-name>.git 
```

### Test your connection

```shell
ssh-keyscan github.com >> ~/.ssh/known_hosts
ssh -T git@github.com-hainghia
ssh -T git@github-hohainghia
```

## [Redis](https://developer.redis.com/create/homebrew/)

- [RedisInsight - Developer GUI for Redis, by Redis](https://github.com/RedisInsight/RedisInsight)
- [Create a Redis database on Mac OS](https://developer.redis.com/create/homebrew/)
- [Redis in a Docker container](https://developer.redis.com/create/docker)
- [[Bug]: Can't connect to ElastiCache Redis Cluster](https://github.com/RedisInsight/RedisInsight/issues/2355)
- [Another Redis Desktop Manager](https://github.com/qishibo/AnotherRedisDesktopManager)

```shell
 brew tap redis-stack/redis-stack
 brew install --cask redis-stack
 echo $PATH
```

*:rocket::rocket::rocket: A faster, better and more stable redis desktop manager, compatible with Linux, windows, mac.
What's more, it won't crash when loading massive keys.*
Tool connect redis

```shell
brew install --cask another-redis-desktop-manager
```

*If you can't open it after installation by brew or dmg, exec the following command then reopen*

```shell
sudo xattr -rd com.apple.quarantine /Applications/Another\ Redis\ Desktop\ Manager.app
```