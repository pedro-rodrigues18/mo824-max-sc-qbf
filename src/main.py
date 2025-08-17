import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.max_sc_qbf import MaxSetCoverQBF


def main() -> None:
    # Read input data
    path = "input/example-02.txt"

    msc_qbf = MaxSetCoverQBF(path)

    msc_qbf.solve()


if __name__ == "__main__":
    main()
