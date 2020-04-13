for _ in range(int(input())):
    n = int(input())
    a = int(input())
    maxi = 10**n - 1
    # printing s
    print(a + 2*maxi + 2)
    b = int(input())
    # printing c
    print(maxi - b + 1)
    d = int(input())
    # printing e
    print(maxi - d + 1)
    ans = int(input())
    if ans == -1:
        exit()
