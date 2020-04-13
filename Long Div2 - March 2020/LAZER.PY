import sys
import time
import numpy
input = sys.stdin.readline
fuck_you_memory = [0]*1000000
for _ in range(int(input())):
    n,q = list(map(int, input().split()))
    hfjjjjf = list(map(int, input().split()));hhhfutne = [];i = 0
    while(i<n-1):
        jjj = min(hfjjjjf[i], hfjjjjf[i+1])
        kkk = max(hfjjjjf[i], hfjjjjf[i+1])
        hhhfutne.append(((jjj, kkk)))
        i = i + 1
    i = 0
    while(i < q):
        ff1, jjjf4, y = list(map(int, input().split()))
        a = (ff1, y); b = (jjjf4, y);
        hhhfhhffyhtht = 0
        for k in range(ff1-1, jjjf4-1):
            left = (k+1,hhhfutne[k][0])
            right = (k+2, hhhfutne[k][1])
            if left == b:
                continue
            if right == a:
                continue
            if y >= hhhfutne[k][0] and y<= hhhfutne[k][1]:
                hhhfhhffyhtht += 1
        print(hhhfhhffyhtht)
        i+=1