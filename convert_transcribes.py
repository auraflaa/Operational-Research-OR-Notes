"""Convert all NPTEL lecture transcribes (PDF) to Markdown with images.
Uses pymupdf4llm - lightweight, runnable locally (pip install pymupdf4llm).
Run with: pdfenv/Scripts/python.exe convert.py
"""
import os
import re
from pathlib import Path
import pymupdf4llm

ROOT = Path(__file__).parent
SRC = ROOT / "Transcribes"       # source PDFs (git-ignored, not pushed)
OUT = ROOT / "transcribe_md"
IMG_ROOT = OUT / "images"  # images per lecture: transcribe_md/images/lec1/...
COURSE_URL = "https://onlinecourses.nptel.ac.in/e-learning/course/noc26_ma85"

OUT.mkdir(exist_ok=True)
IMG_ROOT.mkdir(exist_ok=True)

# NOTE: pymupdf4llm resolves `image_path` relative to the current working
# directory, while the ![](...) refs are written verbatim. So run from OUT:
# image_path="images/lec1" -> files land in transcribe_md/images/lec1 AND the
# refs "images/lec1/..." resolve correctly relative to transcribe_md/*.md.
os.chdir(OUT)

def lec_num(p: Path) -> int:
    m = re.search(r"lec(\d+)", p.stem, re.IGNORECASE)
    return int(m.group(1)) if m else 0

pdfs = sorted(SRC.glob("lec*.pdf"), key=lec_num)
print(f"Found {len(pdfs)} PDFs")

for pdf in pdfs:
    n = lec_num(pdf)
    name = f"lec{n}"
    img_dir_rel = f"images/{name}"          # relative to transcribe_md/*.md
    img_dir_abs = OUT / img_dir_rel
    img_dir_abs.mkdir(parents=True, exist_ok=True)
    out_md = OUT / f"{name}.md"

    print(f"[{n}/40] {pdf.name} -> {out_md.relative_to(ROOT)} ...")
    md_text = pymupdf4llm.to_markdown(
        str(pdf),
        write_images=True,
        image_path=str(img_dir_rel),  # written verbatim into ![](...) refs
        image_format="png",
        dpi=200,
        page_chunks=False,
    )
    # Fix common ligature/encoding glitch: isolated replacement char -> en dash
    md_text = md_text.replace("�", "–")

    frontmatter = (
        "---\n"
        f"lecture: {n}\n"
        f"source_pdf: Transcribes/{pdf.name}\n"
        f"course: {COURSE_URL}\n"
        "---\n\n"
    )
    out_md.write_text(frontmatter + md_text, encoding="utf-8")

print("DONE. Output in", OUT)
