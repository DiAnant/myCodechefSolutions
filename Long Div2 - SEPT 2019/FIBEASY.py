logs = [eval('2**{}'.format(i)) for i in range(72)]

def fibo():
    x0, x1 = 0, 1
    alist = [x0, x1]
    for _ in range(2,60):
        x = (x0 + x1)%10
        x0, x1 = x1, x
        alist.append(x)
    return alist

def calci(n):
    index = 0
    for i in logs:
        if i >= n:
            if i == n:
                return index
            return index-1
        index +=1

for _ in range(int(input())):
    n = int(input())
    fibs = fibo()
    kim = calci(n)
    two_pow = 2**int(kim)
    num =  two_pow % 60
    print(fibs[num-1])