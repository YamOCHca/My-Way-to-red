def solve():
    mod = 10 ** 9 + 7
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    j = 0
    x = 0
    ans = 1
    for i in range(n):
        while j < n and b[j] < a[i]:
            x += 1
            j += 1
        ans *= x
        x -= 1
        ans %= mod
    print(ans)
 
 
for _ in range(int(input())):
    solve()
