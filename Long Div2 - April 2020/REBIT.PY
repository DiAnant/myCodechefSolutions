import sys
from math import log2, ceil
input = sys.stdin.readline

def swaparr(arr, a,b):
    temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp
def gcd(a,b):
    if a > 0:
        return gcd(b%a, a)
    return b
def primefs(n):
    ## if n == 1
    if n == 1:
        return 1
    ## calculating primes
    primes = {}
    while(n%2 == 0):
        primes[2] = primes.get(2, 0) + 1
        n = n//2
    for i in range(3, int(n**0.5)+2, 2):
        while(n%i == 0):
            primes[i] = primes.get(i, 0) + 1
            n = n//i
    if n > 2:
        primes[n] = primes.get(n, 0) + 1
    ## prime factoriazation of n is stored in dictionary primes

## DISJOINT SET UNINON FUNCTION
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a,b
# find function
def find(x, link):
    while(x != link[x]):
        x = link[x]
    return x
# the union function which makes union(x,y)
# of two nodes x and y
def union(x, y, size, link):
    x = find(x, link)
    y = find(y, link)
    if size[x] < size[y]:
        x,y = swap(x,y)
    if x != y:
        size[x] += size[y]
        link[y] = x

## returns an array of boolean if primes or not
def sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime

## taking integer array input
def int_array():
    return list(map(int, input().split()))

############ ---------------- TEMPLATE ENDS HERE ---------------- ############

def modInverse(a, m) : 
    m0 = m; y = 0; x = 1
    if (m == 1) : 
        return 0
    while (a > 1) : 
        q = a // m 
        t = m; m = a % m 
        a = t; t = y 
        y = x - q * y; x = t 
    if (x < 0) : 
        x = x + m0 
    return x 

def power(x, y, p) : 
    res = 1 
    x = x % p  
    if (x == 0) : 
        return 0
    while (y > 0) : 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
    return res 

def probs(a, b, ops):
    this = ['0', '1', 'a', 'A']; mod = 998244353; 
    poss = [(0,0), (1,1), (0,1), (1,0)]
    ans = [0, 0, 0, 0];
    for i in range(4):
        for j in range(4):
            if this[i] == 'a':
                x1 = 0; x2 = 1;
            elif this[i] == 'A':
                x1 = 1; x2 = 0;
            else:
                x1 = int(this[i]); x2 = int(this[i]);

            if this[j] == 'a':
                y1 = 0; y2 = 1;
            elif this[j] == 'A':
                y1 = 1; y2 = 0;
            else:
                y1 = int(this[j]); y2 = int(this[j]);
            if ops == '^':
                xx1 = x1^y1; xx2 = x2^y2;
            elif ops == '&':
                xx1 = x1&y1; xx2 = x2&y2;
            elif ops == '|':
                xx1 = x1|y1; xx2 = x2|y2;
            ours = (xx1, xx2)
            ans[poss.index(ours)] += a[i] * b[j]
    for i in range(len(ans)):
        ans[i] = ans[i]%mod
    return ans

for _ in range(int(input())):
    string = input().strip();
    count = 0;
    pstack = []; ops = []; p = 1;
    for i in string:
        if i == '(':
            pass
        elif i == '#':
            pstack.append([1,1,1,1])
        elif i in '^&|':
            count += 1;
            ops.append(i);
        elif i == ')':
            y = pstack.pop();
            x = pstack.pop();
            op =  ops.pop();
            answer = probs(x, y, op)
            pstack.append(answer);
    mod = 998244353
    count += 1;
    count = power(4, count, mod);
    this = modInverse(count, mod);
    kkk = pstack[0];
    for i in range(4):
        kkk[i] = (kkk[i]*this)%mod
    print(*kkk);
