for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    ass  = list(map(int, input().split()))
    for i in range(k%(3*n)):
        aind = i%n
        bind = n - aind - 1
        ass[aind] = ass[aind]^ass[bind]
    if n == 1:
        print(0)
    elif n % 2 != 0:
        if k > n//2:
            ass[n//2] = 0
        print(' '.join(list(map(str, ass))))
    else:
        print(' '.join(list(map(str, ass))))