for _ in range(int(input())):
    n,m,q = list(map(int, input().split()))
    row = [0 for _ in range(n)]
    col = [0 for _ in range(m)]
    for _ in range(q):
        a, b = list(map(int, input().split()))
        row[a-1] += 1
        col[b-1] += 1
    even1, even2, odd1, odd2 = 0, 0, 0, 0
    for i in row:
        if i % 2 == 0:
            even1 += 1
    for i in col:
        if i % 2 == 0:
            even2 += 1
    odd1 = len(row) - even1
    odd2 = len(col) - even2
    ans = odd1*even2 + odd2*even1
    print(ans)