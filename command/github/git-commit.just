[group('Git')]
git-config:
    @echo "{{YELLOW}}Configuring git for current repository...{{NORMAL}}"
    git config user.email "hohainghia19@gmail.com"
    git config user.name "Hai Nghia"
    git config --list | cat

[group('Git')]
git-commit-push message="":
    #!/usr/bin/env zsh
    set -euo pipefail

    local GIT_USER_NAME="$(git config user.name)" || "unknown"
    local GIT_DATE="$(date +'%Y-%m-%d %H:%M:%S')"
    local DEFAULT_COMMIT_MSG="${GIT_USER_NAME} ${GIT_DATE}"

    if [ -z "{{message}}" ]; then
        local msg="${DEFAULT_COMMIT_MSG}"
    else
        local msg="{{message}}"
    fi

    echo "Pushing changes with message: ${msg}"
    git add .
    git commit --message "${msg}" || echo -e "{{WHITE}}No changes to commit{{NORMAL}}"
    git push
    echo -e "{{GREEN}}✅ Changes pushed successfully!{{NORMAL}}"