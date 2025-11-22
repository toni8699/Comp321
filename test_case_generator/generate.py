#!/usr/bin/env python3
import random
from bisect import bisect_left
from pathlib import Path

SAMPLE_DIR = Path("../data/sample")
SECRET_DIR = Path("../data/secret")
RNG = random.Random(314159)
TOTAL_BYTES_LIMIT = 1_000_000  # total size budget for all .in files


def compute_answers(counts, queries):
    prefix = []
    running = 0
    for value in counts:
        running += value
        prefix.append(running)

    if not prefix:
        return ["impossible"] * len(queries)

    total = prefix[-1]
    answers = []
    for query in queries:
        if query < 1 or query > total:
            answers.append("impossible")
            continue
        idx = bisect_left(prefix, query)
        answers.append(str(idx + 1))
    return answers


def solve_and_save(folder, idx, counts, queries):
    answers = compute_answers(counts, queries)

    folder.mkdir(parents=True, exist_ok=True)
    prefix = f"{folder.name}{idx:02d}"

    (folder / f"{prefix}.in").write_text(
        f"{len(counts)} {len(queries)}\n"
        f"{' '.join(map(str, counts))}\n"
        f"{' '.join(map(str, queries))}\n"
    )
    (folder / f"{prefix}.ans").write_text("\n".join(answers) + "\n")


# Sample cases
samples = [
    ([3, 1, 10, 2, 6], [1, 3, 4, 11, 16]),
    ([5], [1, 5]),
    ([2, 8, 4], [2, 9, 14]),
]

secrets = [
    ([1] * 20, list(range(1, 21))),
    ([7, 3, 9, 1, 4, 6, 2, 5], [1, 7, 10, 11, 25, 37]),
    ([10, 5, 8, 6, 3], [1, 10, 11, 27, 32]),
    ([10, 100, 5], [1, 10, 57, 100, 115]),
    ([1_000_000_000], [1, 500_000_000, 1_000_000_000]),
    ([2] * 1000, [1, 200, 1999, 2000]),
]


def estimate_case_size(counts, queries):
    header = f"{len(counts)} {len(queries)}\n"
    counts_line = " ".join(map(str, counts)) + "\n"
    queries_line = " ".join(map(str, queries)) + "\n"
    return len(header) + len(counts_line) + len(queries_line)


current_bytes = sum(estimate_case_size(c, q) for c, q in samples + secrets)
generated = []

while current_bytes < TOTAL_BYTES_LIMIT:
    if RNG.random() < 0.3:
        n = RNG.randint(50_000, 120_000)
        q = RNG.randint(50_000, 120_000)
        counts = [RNG.randint(1, 1000) for _ in range(n)]
    else:
        n = RNG.randint(1, 5000)
        q = RNG.randint(1, 5000)
        counts = [RNG.randint(1, 1_000_000) for _ in range(n)]
    total = sum(counts)
    queries = [RNG.randint(1, total) for _ in range(q)]

    case_size = estimate_case_size(counts, queries)
    if current_bytes + case_size > TOTAL_BYTES_LIMIT:
        break
    current_bytes += case_size
    generated.append((counts, queries))


if __name__ == "__main__":
    for i, (counts, queries) in enumerate(samples, 1):
        solve_and_save(SAMPLE_DIR, i, counts, queries)

    offset = len(secrets)
    for i, (counts, queries) in enumerate(secrets, 1):
        solve_and_save(SECRET_DIR, i, counts, queries)

    for j, (counts, queries) in enumerate(generated, offset + 1):
        solve_and_save(SECRET_DIR, j, counts, queries)

    total_secret_cases = len(secrets) + len(generated)
    print(f"Generated {len(samples)} sample and {total_secret_cases} secret cases.")