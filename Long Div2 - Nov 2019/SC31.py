for _ in range(int(input())):
    n = int(input())
    strings = []
    for _ in range(n):
        strings.append(input())
    for i in range(n-1):
        this = int(strings[i], 2)^int(strings[i+1], 2)
        xors = '{0:0{1}b}'.format(this,10)
        strings[i+1] = xors
    ans = strings[n-1].count('1')
    print(ans)