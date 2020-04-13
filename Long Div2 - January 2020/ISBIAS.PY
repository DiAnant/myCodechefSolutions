n,q = list(map(int, input().split()))
array = list(map(int, input().split()))
matrix = [[0,0] for _ in range(n)]
current_inc = 0
prev = None
l = 1
incs = 0
decs = 0
for i in range(0, n):
    if i == 0:
        prev = array[i]
        matrix[i] = [incs, decs]
    if i == 1:
        if array[i] > prev:
            incs += 1
            prev = array[i]
            current_inc = 1
            matrix[i] = [incs, decs]
            continue
        else:
            decs += 1
            prev = array[i]
            current_inc = 0
            matrix[i] = [incs, decs]
            continue
    if array[i] > prev:
        prev = array[i]
        if current_inc == 0:
            incs += 1
            current_inc = 1
            matrix[i] = [incs, decs]
        else:
            matrix[i] = [incs, decs]
            continue
    else:
        prev = array[i]
        if current_inc == 0:
            matrix[i] = [incs, decs]
            continue
        else:
            decs += 1
            current_inc = 0
            matrix[i] = [incs, decs]
for _ in range(q):
    l,r = list(map(int, input().split()))
    if l == 1:
        a = matrix[r-1][0] - matrix[l-1][0]
        b = matrix[r-1][1] - matrix[l-1][1]
        if a == b:
            print('YES')
        else:
            print('NO')
    else:
        pre, post = 0,0
        if array[l-2] < array[l-1]:
            pre = 1
        if array[l-1] < array[l]:
            post = 1
        if pre == post:
            a = matrix[r-1][0] - matrix[l-1][0]
            b = matrix[r-1][1] - matrix[l-1][1]            
            if post == 1:
                a += 1
            else:
                b += 1
            if a == b:
                print('YES')
            else:
                print('NO')
        else:
            a = matrix[r-1][0] - matrix[l-1][0]
            b = matrix[r-1][1] - matrix[l-1][1]            
            if a == b:
                print('YES')
            else:
                print('NO')