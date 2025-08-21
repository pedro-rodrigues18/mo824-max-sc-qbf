import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.max_sc_qbf import MaxSetCoverQBF


def main() -> None:
    debug = False  # Set to True for debugging

    # Read input data
    path = "input/"

    # Solve MSC-QBF for each instance
    if not debug:
        for i in range(1, 16):
            instance = f"instance-{i:02d}.txt"
            full_path = Path(path) / instance
            if full_path.exists():
                msc_qbf = MaxSetCoverQBF(full_path)
                msc_qbf.solve(instance)
            else:
                print(f"{instance} does not exist.")
    else:
        # Debugging mode: solve a specific instance
        instance = "ex-01.txt"
        full_path = Path(path) / instance
        if full_path.exists():
            msc_qbf = MaxSetCoverQBF(full_path)
            msc_qbf.solve(instance)
        else:
            print(f"{instance} does not exist.")


if __name__ == "__main__":
    main()
