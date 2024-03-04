#!/usr/bin/env python3
import sys
from pathlib import Path


def normalize(path: Path) -> None:
    print(f"Normalizing file {path}")
    with open(path) as f:
        lines = f.read().split("\n")
    offsets = None
    for index, line in enumerate(lines):
        splitup = line.split(",")
        try:
            offsets = float(splitup[0]), float(splitup[1]), float(splitup[2])
            break
        except:
            pass
    if offsets is None:
        print(f"{path} does not have the expected format. Skipping.")
        return
    print(f"Normalizing with t0={offsets[0]}, x0={offsets[1]}, y0={offsets[2]}")
    for i in range(index, len(lines)):
        if not lines[i]:
            continue
        raw = [float(entry) for entry in lines[i].split(",")]
        lines[i] = ",".join(
            (f"{entry - offsets[j]:.3f}" for j, entry in enumerate(raw))
        )
    with open(path, "w") as f:
        f.write("\n".join(lines))


def main() -> int:
    """
    Main starting point of script.

    :return: An exit code, 0 on success.
    """
    for file in Path("data").iterdir():
        if not file.is_file():
            continue
        normalize(file)
    return 0


if __name__ == "__main__":
    sys.exit(main())
