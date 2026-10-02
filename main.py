"""Hex Color Export — Collect hex colors from a CSS or SVG file and write a palette sheet."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='hex_color_export',
        description='Collect hex colors from a CSS or SVG file and write a palette sheet.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Hex Color Export')
    print('Pull a palette out of existing CSS.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
