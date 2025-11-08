set dotenv-load := true
set shell := ["zsh", "-uc"]

import? 'command/__init__.just'

# Defaul recipe to run when no arguments are provided
default:
    @just --fmt --unstable
    @just --list

# Generate .env file from environment variables
env-generate:
    @uv run --module src.python.cli.gen_dotenv
    @echo "{{ GREEN }}APP_NAME::{{ NORMAL }}{{ BOLD + MAGENTA }}${APP_NAME}{{ NORMAL }}"
