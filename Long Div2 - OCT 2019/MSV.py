for _ in range(int(input())):
    n = int(input())
    ass = list(map(int, input().split()))
    dick = dict()
    maxx = -1
    for i in ass:
        dick[1] = dick.get(1,0) + 1
        if i > 1:
            if dick.get(i,0) > maxx:
                maxx = dick.get(i,0)
            dick[i] = dick.get(i,0) + 1
            facts = []
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    dick[j] = dick.get(j,0) + 1
                    if j != i//j:
                        dick[i//j] = dick.get(i//j, 0) + 1     
    print(maxx)