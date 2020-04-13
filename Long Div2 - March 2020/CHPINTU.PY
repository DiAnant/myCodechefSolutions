for kkk in range(int(input())):
    n,m = list(map(int, input().split()));
    fis = list(map(int, input().split()))
    fishfish = list(map(int, input().split()))
    pussy = {}
    t = len(fis)
    for k in range(t):
        i = fis[k]
        this = pussy.get(i, 0)
        pussy[i] = this + fishfish[k]
    ans = 1e20
    for i in pussy:
        ans = min(ans, pussy[i])
    print(ans)