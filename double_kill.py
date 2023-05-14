import queue
import sys
import math


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        dp = [[0, 0] for i in range(n)]
        for j in range(i, n):
            dp[j][0] = max(dp[j - 1][0], a[j])
            l, r = i - 1, j
            while r - l > 1:
                m = (r + l) // 2
                if dp[m][0] > a[j]:
                    r = m
                else:
                    l = m
            x = j - r + dp[l][1]
            if j == i or a[j] < a[j - 1] or dp[j - 1][1] == 0 or a[j] > dp[j - 1][0]:
                ans += x
                dp[j][1] = x
            else:
                ans += dp[j - 1][1] + 1
                dp[j][1] = dp[j - 1][1] + 1
        print(*dp)
    print(ans)


for _ in range(int(input())):
    solve()
