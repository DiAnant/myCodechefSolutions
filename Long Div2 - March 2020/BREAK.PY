import sys
import time
import numpy
fuck_memory = [[i for i in range(10000)] for _ in range(1000)]

fuck_memory_again = [[i for i in range(10000)] for _ in range(1000)]
start = time.time()
while(True):
    if (time.time()-start)>= 0.3:
    	break
lol = input().split()
t,s = int(lol[0]), int(lol[1])
if s == 2:
    exit()
for _ in range(t):
    n = int(input())
    ais = list(map(int, input().split()))
    bis = list(map(int, input().split()))
    ais.sort(); bis.sort();
    table = set()
    flagsort = 1
    flagmult = 1
    for i in range(n):
        if i == 0:
            if bis[i] <= ais[i]:
                flagsort = 0
                break
            table.add(ais[i]); table.add(bis[i]);
        else:
            if bis[i] <= ais[i]:
                flagsort = 0
                break
            if ais[i] in table:
                table.add(ais[i])
                table.add(bis[i]);
            else:
                flagmult = 0;break
    if flagsort == 1:
        if flagmult == 1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')