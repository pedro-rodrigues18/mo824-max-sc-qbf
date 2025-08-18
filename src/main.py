import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.max_sc_qbf import MaxSetCoverQBF


def main() -> None:
    # Read input data
    path = "input/"

    # Solve MSC-QBF for each instance
    for i in range(1, 16):
        instance = f"instance-{i:02d}.txt"
        full_path = Path(path) / instance
        print(full_path)
        if not full_path.exists():
            print(f"Instance {instance} does not exist.")
            continue
        msc_qbf = MaxSetCoverQBF(full_path)
        msc_qbf.solve(instance)


if __name__ == "__main__":
    main()
