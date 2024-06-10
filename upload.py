import json
import os
from pathlib import Path

from deta import Deta

DETA_KEY = os.getenv('DETA_KEY')
assert DETA_KEY, 'set DETA_KEY env, stupid'

base = Deta(DETA_KEY).Base('nonograms')

nonograms_file = Path("nonograms.json")
nonograms = json.loads(nonograms_file.read_text())

uploaded = 0
for nonogram in nonograms:
    base.put(nonogram, key=nonogram["title"])
    uploaded += 1
    print(f"{uploaded} nonograms uploaded")
