![Hex Color Export](assets/hero.png)

# Hex Color Export

*Pull a palette out of existing CSS.*

## Overview

**Hex Color Export** runs on your own PC. Collect hex colors from a CSS or SVG file and write a palette sheet.

A legacy stylesheet has the brand colors buried in 40 files.

Files stay on the machine that runs the tool. Originals are left alone unless you choose otherwise.

## Editions

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## What it does

- Scan CSS and SVG
- Unique hex list
- PNG palette sheet
- Optional JSON dump

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```text
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Install

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/jjackson-9231/hex-color-export

MIT license. See `LICENSE`.
