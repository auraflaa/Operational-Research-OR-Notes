# Operations Research — NPTEL Exam Notes (noc26_ma85)

Study notes for the NPTEL course **Operations Research** by Prof. Kusum Deep, IIT Roorkee (40 lectures).
Course page: https://onlinecourses.nptel.ac.in/e-learning/course/noc26_ma85

Start here: [`Notes/README.md`](Notes/README.md) (index + exam strategy), then read the module files.

## Repo layout

| Path | Contents |

|---|---|

| `Notes/` | Detailed module-wise exam notes (start with `Notes/README.md`) |

| `Notes/figures/` | Flowcharts (`m*.png`, from LaTeX-TikZ sources in `tex/`) and matplotlib/seaborn graphs (`g_*.png`, via `make_graphs.py`) |

| `Questions/` | Weekly assignment-style practice sets (Weeks 1–8) + 100-mark mock final, all with answer keys and worked solutions |

| `transcripts/` | Full lecture transcripts in Markdown (`lec1.md`–`lec40.md`) with slide images under `transcripts/images/lecN/` |

| `source_pdfs/` | Source lecture PDFs — **kept locally only, git-ignored, not pushed** |

| `convert_pdfs_to_md.py` | Script that converts `source_pdfs/*.pdf` into `transcripts/` (requires `pymupdf4llm` + `pillow`) |

## Regenerating

- Transcripts: place the 40 lecture PDFs in `source_pdfs/` and run `convert_pdfs_to_md.py` (see its docstring).
- Graphs: run `Notes/figures/make_graphs.py` (requires `matplotlib`, `seaborn`).
- Flowcharts: edit a `.tex` source in `Notes/figures/tex/`, compile with a LaTeX engine (e.g. Tectonic: `tectonic -o <dir> <file>.tex`), convert the PDF to PNG.

## Source credit and license

Lecture content belongs to NPTEL / Prof. Kusum Deep, IIT Roorkee. These notes are an independent study aid.
The notes, transcript formatting, figures and scripts in this repository are licensed under
[CC BY-SA 4.0](LICENSE) — share freely with attribution, and share adaptations under the same terms.
