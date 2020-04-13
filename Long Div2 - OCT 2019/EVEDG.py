for _ in range(int(input())):
    n, m = list(map(int, input().split()))
    array = [0]*n
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a,b = list(map(int, input().split()))
        array[a-1] += 1
        array[b-1] += 1
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    flag = True
    for i in array:
        if i % 2 != 0:
            flag = False
            break
    if m % 2 == 0:
        print(1)
        print(' '.join(['1' for _ in range(n)]))
    elif flag == True:
        this = ['1' for _ in range(n)]
        for j in range(len(array)):
            if len(graph[j]) > 0:
                this[j] = '2'
                this[graph[j][0]] = '3'
                break
        print(3)
        print(' '.join(this))
    else:
        if array[0] % 2 != 0:
            this = ['2' for _ in range(n)]
            this[0] = '1'
        else:        
            this = ['1' for _ in range(n)]
            for i in range(n):
                if array[i] %2 != 0:
                    this[i] = '2'
                    break
        print(2)
        print(' '.join(this))