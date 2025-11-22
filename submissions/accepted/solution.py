N, Q = map(int, input().split())
piles = list(map(int, input().split()))
q = list (map(int, input().split()))

prefix = []
cur = 0
for value in piles:
    cur += value
    prefix.append(cur)

def binary_search(arr, target):
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo

total = prefix[-1]
for query in queries:
    if query > total or query < 1:
        print("impossible")
    else:
        print(binary_search(prefix, query))