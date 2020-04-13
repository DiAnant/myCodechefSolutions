import sys
import numpy
import time
fuck_you_memory = [i for i in range(1000000)]
shmuck_you_memory = [i for i in range(1000000)]
suck_you_memory = [i for i in range(1000000)]
ans = [(2, 2),(3, 1),(1, 3),(2, 4),
 (1, 5),
 (5, 1), (6, 2),(7, 1),
 (1, 7),
 (2, 8),
 (8, 2),
 (7, 3),
 (8, 4),
 (4, 8),
 (5, 7),
 (6, 8),
 (8, 6),
 (7, 7),
 (8, 8)]

for _ in range(int(input())):
    r,c = list(map(int, input().split()))
    if r!=1 or c!=1 :
        if r == c:
            print(19+1)
            print(1,1)
            for i in ans:
                print(*i)
        else:
            print(19+2)
            k = int((r+c)/2)
            print(k,k)
            print(1,1)
            for i in ans:
                print(*i)
    else:
        print(19)
        for i in ans:
            print(*i)
            
            
        