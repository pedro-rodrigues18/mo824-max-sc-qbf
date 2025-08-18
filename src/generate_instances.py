import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


def generate_subsets(n):
    N = set(range(1, n + 1))
    S = []

    covered = set()
    for i in range(n):
        size = random.randint(2, n)  # random size >= 2
        subset = set(random.sample(range(1, n + 1), size))
        S.append(subset)
        covered.update(subset)

    missing = N - covered
    if missing:
        S[-1] = S[-1].union(missing)

    return S


def generate_instances(n) -> str:
    S = generate_subsets(n)

    lines = []
    lines.append(str(n))  # number of elements
    lines.append(" ".join(str(len(s)) for s in S))  # sizes of the subsets

    for s in S:
        lines.append(" ".join(map(str, sorted(s))))  # elements of each subset

    # random sequences with decreasing sizes
    number = n
    while number >= 1:
        line = " ".join(str(random.randint(-10, 10)) for _ in range(number))
        lines.append(line)
        number -= 1

    return "\n".join(lines)


def main():
    path = "input"

    size_of_instances = [25, 50, 100, 200, 400]
    cont = 1
    for size in size_of_instances:
        for i in range(3):
            lines = generate_instances(size)
            with open(f"{path}/instance-{cont:02d}.txt", "w") as f:
                try:
                    f.write(lines)
                    print(
                        f"File {path}/instance-{cont:02d}.txt successfully generated."
                    )
                except Exception as e:
                    print(f"Error writing to file: {e}")
                    continue
            cont += 1


if __name__ == "__main__":
    main()
