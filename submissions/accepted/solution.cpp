#include <iostream>
#include <vector>

int lowerBound(const std::vector<long long>& arr, long long target);

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, Q;
    if (!(std::cin >> N >> Q)) {
        return 0;
    }

    std::vector<long long> piles(N);
    for (int i = 0; i < N; ++i) {
        std::cin >> piles[i];
    }

    std::vector<long long> queries(Q);
    for (int i = 0; i < Q; ++i) {
        std::cin >> queries[i];
    }

    std::vector<long long> prefix(N);
    long long running = 0;
    for (int i = 0; i < N; ++i) {
        running += piles[i];
        prefix[i] = running;
    }

    long long total = prefix.back();
    for (long long target : queries) {
        if (target < 1 || target > total) {
            std::cout << "impossible\n";
        } else {
            int idx = binarySearch(prefix, target);
            std::cout << idx << "\n";
        }
    }

    return 0;
}

int binarySearch(const std::vector<long long>& arr, long long target) {
    int lo = 0;
    int hi = static_cast<int>(arr.size());
    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] >= target) {
            hi = mid;
        } else {
            lo = mid + 1;
        }
    }
    return lo;
}

