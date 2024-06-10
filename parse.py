"""
catalogue "gnonograms 42.gno"
title "Meaning of life the universe and"
by "Frederico Vera <dktcoding@gmail.com>"
copyright "© 2010 Frederico Vera <dktcoding@gmail.com>"
license CC-BY-SA-4.0
height 23
width 35

rows
3
5,8
6,11
7,13
8,7,5

columns
2
4
6
7
8
10
11
7,4

goal "0000000000011100000000000000000000000000000001111100000000011111111000000000000111111000000011111111111000000000011111110000001111111111111000000001111111100000111111100111110000000011111111000001111100000111100000001111111110000011100000001111000000111110111100000000000000011110000001111001111000000000000001111100000111110011110000000000000111111000011111000111100000000000011111100001111100001111000000000011111110000011111000011110000000001111111000001111111111111111000000111111000000111111111111111111000011111100000001111111111111111110001111100000000001111111111111111000111110000000000000000000001111000001111000000000000000000000011110000011110000000000000000000000111100000111111111111100000000000001111000001111111111111110000000000011110000011111111111111100000000000111100000011111111111110"
"""

import json
from pathlib import Path
from typing import Any

nonogram_db = Path('nonogram-db-master')

nonograms: dict[str, Any] = []
for file in nonogram_db.glob('**/*.non'):
    print(file)

    lines = file.read_text().splitlines()

    catalogue = lines.pop(0).split(maxsplit=1)[1].strip('"')
    title = lines.pop(0).split(maxsplit=1)[1].strip('"')
    by = lines.pop(0).split(maxsplit=1)[1].strip('"')
    copyright_ = lines.pop(0).split(maxsplit=1)[1]
    license_ = lines.pop(0).split(maxsplit=1)[1]
    height = int(lines.pop(0).split(maxsplit=1)[1])
    width = int(lines.pop(0).split(maxsplit=1)[1])

    rows: list[tuple[int]] = []
    columns: list[tuple[int]] = []

    while (line := lines.pop(0)) not in {'rows', 'columns'}:
        pass

    target = rows if line == 'rows' else columns
    while (line := lines.pop(0)) and line not in {'rows', 'columns'}:
        cells = tuple(int(c) for c in line.split(','))
        target.append(cells)

    while (line := lines.pop(0)) not in {'rows', 'columns'}:
        pass

    target = rows if line == 'rows' else columns
    while (line := lines.pop(0)) and not line.startswith('goal'):
        cells = tuple(int(c) for c in line.split(','))
        target.append(cells)

    while not line.startswith('goal'):
        line = lines.pop(0)

    goal_str = line.removeprefix('goal').strip('" ')

    goal: list[list[bool]] = []
    for y in range(height):
        row_slice = goal_str[(y * width):(y * width + width)]
        row = [c == '1' for c in row_slice]
        goal.append(row)

    nonogram = {
        'catalogue': catalogue,
        'title': title,
        'by': by,
        'copyright': copyright_,
        'license': license_,
        'height': height,
        'width': width,
        'rows': rows,
        'columns': columns,
        'goal': goal,
    }
    nonograms.append(nonogram)

nonograms_file = Path("nonograms.json")
nonograms_file.write_text(json.dumps(nonograms))
