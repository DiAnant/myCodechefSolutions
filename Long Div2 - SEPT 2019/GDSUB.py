import sys
def freq(array):
    freaky = [array.count(i) for i in list(set(array))]
    return freaky

def mod(n):
    if n < 0:
        n+=1000000007
    else:
        n = n % 1000000007
    return n

n, k = list(map(int, input().strip().split()))
array = list(map(int, input().strip().split()))
# n ,k = 8000, 500
# array = [i+1 for i in range(8000)]

freak = freq(array)
nlen = len(freak)
if k >= nlen:
    res = 1
    for i in freak:
        res = mod(res * (i+1))
    print(int(mod(res)))
    sys.exit() 
if k == 1:
    kuss = sum(freak) + 1
    print(int(mod(kuss)))
    sys.exit()
dp = [[0]*nlen for _ in range(k)]
# making row 1 of dp array same as array
dp[0] = freak.copy()
for length in range(1, k):
    for ind in range(0, nlen-length):
        dp[length][ind] = mod(sum(dp[length-1][ind+1:]) * freak[ind])
ans = sum([sum(i) for i in dp]) + 1 ## 1 for the null fucking set
print(int(mod(ans)))