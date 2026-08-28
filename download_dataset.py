from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dataset"
OUT.mkdir(parents=True, exist_ok=True)

# Official UCI download for Dataset 320
URL = "https://archive.ics.uci.edu/static/public/320/student%2Bperformance.zip"

print("Downloading the official UCI Student Performance archive...")
with urlopen(URL) as response:
    data = response.read()

with ZipFile(BytesIO(data)) as z:
    names = z.namelist()
    math_file = next(name for name in names if name.endswith("student-mat.csv"))
    content = z.read(math_file)

# Keep the original semicolon-separated format used by UCI.
target = OUT / "student-mat.csv"
target.write_bytes(content)

print(f"Saved official Mathematics dataset to: {target}")
