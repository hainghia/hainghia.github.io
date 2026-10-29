from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader

SCRIPT = Path(__file__).resolve().parents[1] / "command/export_resume.py"


def _get_env() -> dict[str, str]:
    env = dict(os.environ)
    if (
        "/opt/homebrew/lib" not in env.get("DYLD_FALLBACK_LIBRARY_PATH", "")
        and Path("/opt/homebrew/lib").exists()
    ):
        env["DYLD_FALLBACK_LIBRARY_PATH"] = (
            "/opt/homebrew/lib:" + env.get("DYLD_FALLBACK_LIBRARY_PATH", "")
        ).rstrip(":")
    return env


def test_export_en_pdf(tmp_path: Path) -> None:
    output = tmp_path / "CV export" / "cv en.pdf"
    subprocess.run(
        [sys.executable, str(SCRIPT), str(output)], env=_get_env(), check=True
    )
    reader = PdfReader(output)
    text = "\n".join(page.extract_text() for page in reader.pages)
    assert "ho hai nghia" in text.lower()
    assert "dynamics 365" in text.lower()
    assert "Print / PDF" not in text
    assert "yooz" not in text.lower()
    assert len(reader.pages) > 0
    for i, page in enumerate(reader.pages):
        assert len(page.extract_text().strip()) > 0, f"Page {i + 1} is empty in EN PDF!"
        assert abs(float(page.mediabox.width) - 595.28) < 1
        assert abs(float(page.mediabox.height) - 841.89) < 1


def test_export_vi_pdf(tmp_path: Path) -> None:
    output = tmp_path / "CV export" / "cv vi.pdf"
    subprocess.run(
        [sys.executable, str(SCRIPT), str(output)], env=_get_env(), check=True
    )
    reader = PdfReader(output)
    text = "\n".join(page.extract_text() for page in reader.pages)
    assert "hồ hải nghĩa" in text.lower()
    assert "dynamics 365" in text.lower()
    assert "In / Xuất PDF" not in text
    assert len(reader.pages) > 0
    for i, page in enumerate(reader.pages):
        assert len(page.extract_text().strip()) > 0, f"Page {i + 1} is empty in VI PDF!"
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
