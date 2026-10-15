# Xuất CV EN PDF
[group('Resume')]
[positional-arguments]
resume-pdf output="exports/resume/hainghia-cv-en.pdf":
    #!/usr/bin/env zsh
    set -euo pipefail
    uv run --no-project --with weasyprint==68.0 python command/export_resume.py "$1"
    echo "Đã xuất CV EN: ${1:A}"

_resume-pdf-check:
    #!/usr/bin/env zsh
    set -euo pipefail
    RUN=(uv run --no-project --with weasyprint==68.0 --with pypdf --with pytest --with ruff --with mypy)
    "${RUN[@]}" ruff check command/export_resume.py tests/test_export_resume.py
    "${RUN[@]}" ruff format --check command/export_resume.py tests/test_export_resume.py
    "${RUN[@]}" mypy --strict --ignore-missing-imports command/export_resume.py
    "${RUN[@]}" pytest -q tests/test_export_resume.py



