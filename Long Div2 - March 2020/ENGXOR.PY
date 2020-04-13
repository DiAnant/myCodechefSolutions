import sys
input= sys.stdin.readline

def andfunc(x,y):
    return (x & y)
urkkdnfjf = [0] * 256
def begin(): 
    urkkdnfjf[0] = 0
    for i in range(256): 
        urkkdnfjf[i] = andfunc(i, 1) + urkkdnfjf[i // 2] 
def countSetBits(n): 
    return (urkkdnfjf[andfunc(n,0xff)] +
            urkkdnfjf[andfunc((n >> 8), 0xff)] +
            urkkdnfjf[andfunc((n >> 16), 0xff)] +
            urkkdnfjf[n >> 24]) 
begin()
kkkkkk = int(input())
for _ in range(kkkkkk):
    n, q = list(map(int, input().split()))
    array = list(map(int, input().split()));jvnjfng = 0;iiiiiiiingjgn = 0;index = 0
    while(index < len(array)):
        i = array[index]
        kkk = countSetBits(i)%2
        if (kkk != 0):
            iiiiiiiingjgn += 1
        else:
            jvnjfng += 1
        index += 1
    for _ in range(q):
        p = int(input())
        thisev = 0
        ansod = 0;
        flag = True
        if(countSetBits(p)%2 == 0):
            pass
        else:
            flag = False
        if flag:
            print(jvnjfng, iiiiiiiingjgn)
        else:
            print(iiiiiiiingjgn, jvnjfng)