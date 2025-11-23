import java.util.Scanner;

public class solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextInt()) {
            sc.close();
            return;
        }

        int N = sc.nextInt();
        int Q = sc.nextInt();

        long[] piles = new long[N];
        for (int i = 0; i < N; ++i) {
            piles[i] = sc.nextLong();
        }

        long[] queries = new long[Q];
        for (int i = 0; i < Q; ++i) {
            queries[i] = sc.nextLong();
        }

        sc.close();

        long[] prefix = new long[N];
        long running = 0;
        for (int i = 0; i < N; ++i) {
            running += piles[i];
            prefix[i] = running;
        }

        long total = N > 0 ? prefix[N - 1] : 0;
        StringBuilder sb = new StringBuilder();
        for (long target : queries) {
            if (target < 1 || target > total) {
                sb.append("impossible\n");
            } else {
                int idx = binarySearch(prefix, target);
                sb.append(idx).append('\n');
            }
        }

        System.out.print(sb.toString());
    }

    private static int binarySearch(long[] arr, long target) {
        int lo = 0;
        int hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (arr[mid] >= target) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        return lo;
    }
}

