from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

SCRIPT = Path(__file__).resolve().parents[1] / "command/export_resume.py"


def test_export_en_pdf(tmp_path: Path) -> None:
    output = tmp_path / "CV export" / "cv en.pdf"
    env = dict(os.environ)
    if (
        "/opt/homebrew/lib" not in env.get("DYLD_FALLBACK_LIBRARY_PATH", "")
        and Path("/opt/homebrew/lib").exists()
    ):
        env["DYLD_FALLBACK_LIBRARY_PATH"] = (
            "/opt/homebrew/lib:" + env.get("DYLD_FALLBACK_LIBRARY_PATH", "")
        ).rstrip(":")
    subprocess.run([sys.executable, str(SCRIPT), str(output)], env=env, check=True)
    reader = PdfReader(output)
    text = "\n".join(page.extract_text() for page in reader.pages)
    assert "Ho Hai Nghia" in text
    assert "Dynamics 365" in text
    assert "Print / PDF" not in text
    assert "yooz" not in text.lower()
    assert len(reader.pages) > 0
    for page in reader.pages:
        assert abs(float(page.mediabox.width) - 595.28) < 1
        assert abs(float(page.mediabox.height) - 841.89) < 1


def test_reject_non_pdf_output(tmp_path: Path) -> None:
    output = tmp_path / "index.html"
    output.write_text("Giữ nguyên", encoding="utf-8")
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(output)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert output.read_text(encoding="utf-8") == "Giữ nguyên"
