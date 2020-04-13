## necessary imports
import sys
import random
from math import log2, log, ceil
input = sys.stdin.readline

# swap_array function
def swaparr(arr, a,b):
    temp = arr[a];
    arr[a] = arr[b];
    arr[b] = temp

## gcd function
def gcd(a,b):
    if a > 0:
        return gcd(b%a, a)
    return b

## prime factorization
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
    ## prime factoriazation of n is stored in dictionary
    ## primes and can be accesed. O(sqrt n)
    return primes

## DISJOINT SET UNINON FUNCTIONS
def swap(a,b):
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

## returns an array of boolean if primes or not USING SIEVE OF ERATOSTHANES
def sieve(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    return prime

#### PRIME FACTORIZATION IN O(log n) using Sieve ####
MAXN = int(1e6 + 5)
def spf_sieve():
    spf[1] = 1;
    for i in range(2, MAXN):
        spf[i] = i;
    for i in range(4, MAXN, 2):
        spf[i] = 2;
    for i in range(3, ceil(MAXN ** 0.5), 2):
        if spf[i] == i:
            for j in range(i*i, MAXN, i):
                if spf[j] == j:
                    spf[j] = i;
    ## function for storing smallest prime factors (spf) in the array

################## un-comment below 2 lines when using factorization #################
spf = [0 for i in range(MAXN)] 
spf_sieve() 
def factoriazation(x):
    ret = {};
    while x != 1:
        ret[spf[x]] = ret.get(spf[x], 0) + 1;
        x = x//spf[x]
    return ret
    ## this function is useful for multiple queries only, o/w use
    ## primefs function above. complexity O(log n)

## taking integer array input
def int_array():
    return list(map(int, input().split()))

################# ---------------- TEMPLATE ENDS HERE ---------------- #################

def dfs(at):
    global parent, visited
    if visited[at]:
        return 
    visited[at] = True
    neighbours = graph[at]
    for this in neighbours:
        if parent[this] == None:
            parent[this] = at
        dfs(this)

for _ in range(int(input())):
    mod = int(1e9+7)
    n = int(input()); edges = [];
    for __ in range(n-1):
        x,y = int_array();
        edges.append((x-1, y-1))
    ## making a graph adjacency list 
    graph = [[] for _ in range(n)]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    a = int_array(); facts = [];
    for i in a:
        facts.append(factoriazation(i));
    q = int(input());
    for __ in range(q):
        x, y = int_array(); x -= 1; y -=1;
        if x == y:
            ans = 1;
            for i in facts[x]:
                ans *= ((facts[x][i]+1) % mod)
            print(ans % mod)
        else:
            parent = [None]*n; visited = [False]*n;
            dfs(x);
            path = [y];
            while(parent[y] != x):
                path.append(parent[y])
                y = parent[y];
            path.append(x);
            total_dick = {}
            for p_path in path:
                for i in facts[p_path]:
                    total_dick[i] = total_dick.get(i, 0) + facts[p_path][i];
            ans = 1;
            for i in total_dick:
                ans *= ((total_dick[i] + 1) % mod)
            print(ans % mod);
