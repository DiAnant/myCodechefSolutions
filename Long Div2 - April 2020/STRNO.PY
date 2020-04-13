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


def pooppoo(n):
    if n == 1:
        return 1
    primes = {}
    while(True):
        if n%2 != 0:
            break
        primes[2] = primes.get(2, 0) + 1
        n = n//2
    for i in range(3, int(n**0.5)+3, 2):
        while(n%i == 0):
            primes[i] = primes.get(i, 0) + 1
            n = n//i
    if n > 2:
        primes[n] = primes.get(n, 0) + 1
    return primes
for _ in range(int(input())):
    x, k = int_array();
    this_dick = pooppoo(x)
    cums = sum(list(this_dick.values())) 
    if cums >= k:
        print(int(True))
    else:
        print(int(False))