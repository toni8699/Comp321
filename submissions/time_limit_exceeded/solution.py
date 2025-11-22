N, Q = map(int, input().split())
piles = list(map(int, input().split()))
queries = list(map(int, input().split()))

for target in queries:
    running = 0
    for i, coins in enumerate(piles, start=1):
        running += coins
        if running >= target:
            print(i)
            break
    else:
        print("impossible")
