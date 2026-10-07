"""Build two independent Pygbag players from their readable Python entrypoints."""
from pathlib import Path
import shutil
import subprocess
import sys

root = Path(__file__).resolve().parent
for name in ("bouncing-ball", "interacting-circles"):
    staging = root / "build" / name
    staging.mkdir(parents=True, exist_ok=True)
    shutil.copy2(root / name / "main.py", staging / "main.py")
    subprocess.run([sys.executable, "-m", "pygbag", "--build", str(staging)], check=True)
    for path in (staging / "build" / "web").iterdir():
        if path.is_file():
            shutil.copy2(path, root / name / path.name)
