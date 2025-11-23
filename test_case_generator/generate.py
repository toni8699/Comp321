#!/usr/bin/env python3
import random
import os
import bisect

RNG = random.Random(2025)
MAX_BYTES = 500 * 1024  # 500KB
MIN_SECRETS = 20

SAMPLES = [
    ([3, 1, 10, 2, 6], [1, 3, 4, 11, 23]), # test all cases 
    ([5], [1, 5]), # test single pile
    ([2, 8, 4], [2, 9, 14]), # test each pile boundary
    ([4, 2, 5], [6, 7, 11]), # test interior hits and out of range 
    ([1, 1, 1, 1], [1, 2, 3, 4,5]), # test uniform piles
]

# TLE Case
TLE_N = 25000 
TLE_COUNTS = [1] * TLE_N 
TLE_QUERIES = [TLE_N + 1] * TLE_N 

HANDPICKED_SECRETS = [
    ([10], [1, 10, 11]),                          # Single pile with 10 coins, 3 queries
    ([1000000] * 5, [1, 1000000, 5000000, 5000001]), # 5 piles of 1,000,000 coins, 4 queries
    ([1] * 1000, [1, 500, 1000, 1001]),           # 1,000 piles of 1 coin, 4 queries
    ([10, 1, 10, 1], [10, 11, 21, 22, 23]),       # 4 piles with varying sizes, 5 queries
    ([500], list(range(1, 502))),                 # Single pile with 500 coins, 501 queries
    (TLE_COUNTS, TLE_QUERIES) #The TLE Case
]

def solve(counts, queries):
    prefix = []
    curr = 0
    for c in counts:
        curr += c
        prefix.append(curr)
    
    total = prefix[-1]
    answers = []
    
    for q in queries:
        if 1 <= q <= total:
            idx = bisect.bisect_left(prefix, q)
            answers.append(str(idx))
        else:
            answers.append("impossible")
    return "\n".join(answers)

def write_case(path, name, idx, counts, queries):
    input_str = f"{len(counts)} {len(queries)}\n" \
                f"{' '.join(map(str, counts))}\n" \
                f"{' '.join(map(str, queries))}\n"
    
    ans_str = solve(counts, queries) + "\n"

    base = f"{path}/{name}{idx:02d}"
    with open(f"{base}.in", "w") as f: f.write(input_str)
    with open(f"{base}.ans", "w") as f: f.write(ans_str)
    return len(input_str)

def main():
    os.makedirs("../data/sample", exist_ok=True)
    os.makedirs("../data/secret", exist_ok=True)

    print("Writing Samples...")
    for i, (c, q) in enumerate(SAMPLES, 1):
        write_case("../data/sample", "sample", i, c, q)

    curr_bytes = 0
    secret_idx = 1

    print("Writing Handpicked Secrets (Including TLE case)...")
    for c, q in HANDPICKED_SECRETS:
        curr_bytes += write_case("../data/secret", "secret", secret_idx, c, q)
        secret_idx += 1

    print("Writing Random Secrets...")
    while curr_bytes < MAX_BYTES or secret_idx <= MIN_SECRETS:
        n_piles = RNG.randint(1, 2000)
        # 20% chance of a large pile
        max_val = 100000 if RNG.random() < 0.2 else 1000 
        counts = [RNG.randint(1, max_val) for _ in range(n_piles)]

        # 10% chance of a large query
        max_query = 1000000000000000000 if RNG.random() < 0.1 else 1000000000
        n_queries = RNG.randint(1, 2000)
        queries = [RNG.randint(1, max_query) for _ in range(n_queries)] 


        curr_bytes += write_case("../data/secret", "secret", secret_idx, counts, queries)
        secret_idx += 1

    print(f"Finished. {secret_idx-1} secrets created. Total size: {curr_bytes/1024:.2f}KB")

if __name__ == "__main__":
    main()