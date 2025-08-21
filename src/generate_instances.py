import random
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))


def generate_subsets(n, pattern=1):
    N = list(range(1, n + 1))
    S = []

    if pattern == 1:
        # Uniform random
        for _ in range(n):
            size = random.randint(2, n)
            subset = set(random.sample(N, size))
            S.append(subset)

    elif pattern == 2:
        # Sequential intervals with overlap
        window = max(3, n // 5)
        # print(f"Window size: {window}")
        for i in range(n):
            subset = set(((i + j) % n) + 1 for j in range(window))
            S.append(subset)

    elif pattern == 3:
        # Clusters
        num_clusters = max(2, n // 10)
        cluster_size = n // num_clusters
        for i in range(n):
            cluster_id = i % num_clusters
            cluster_start = cluster_id * cluster_size + 1
            cluster_end = cluster_start + cluster_size
            cluster_elements = list(range(cluster_start, min(cluster_end, n + 1)))
            # 70% cluster + 30% random
            cluster_pick = random.sample(
                cluster_elements, max(1, int(0.7 * len(cluster_elements)))
            )
            extra_pick = random.sample(N, max(1, int(0.3 * cluster_size)))
            S.append(set(cluster_pick + extra_pick))

    # Ensures coverage of the universe
    covered = set().union(*S)
    missing = set(N) - covered
    if missing:
        S[-1] = S[-1].union(missing)

    return S


def generate_instances(n, pattern) -> str:
    S = generate_subsets(n, pattern)

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
        for pattern in range(1, 4):
            lines = generate_instances(size, pattern)
            with open(f"{path}/instance-{cont:02d}.txt", "w") as f:
                f.write(lines)
            cont += 1


if __name__ == "__main__":
    main()
