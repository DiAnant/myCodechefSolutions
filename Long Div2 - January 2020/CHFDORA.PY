import time
def ispalindrome(arr):
    c = len(arr)
    for i in range(c//2):
        if arr[i] != arr[c-i-1]:
            return False
    return True
def manachar(s):
    n = len(s)
    d = [None]*n
    for i in range(n):
        l = 0
        r = -1
        if i > r:
            k = 1
        else:
            k = min(d[1 + r - 1], r - i + 1)
        while(0 <= i - k and i+k<n and s[i-k]==s[i+k]):
            k+=1
        d[i] = k
        k-=1
        if i+k>r:
            l = i-k
            r = i+k
    return d

def mana(matrix,n,m):
    ans1 = []
    for arr in matrix:
        NOW = time.time()
        if NOW - START > 0.8:
            return 'FUCK'
        ans1.append(manachar(arr))
    ans2 = []
    tatrix = transpose(matrix)
    for arr in tatrix:
        NOW = time.time()
        if NOW - START > 0.8:
            return 'FUCK'
        ans2.append(manachar(arr))
    ans2 = transpose(ans2)
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += min(ans1[i][j],ans2[i][j])
    return ans

def oldie(matrix,n,m):
    count = 0
    for i in range(n):
        for j in range(m):
            size = min(i,n-i-1,j,m-j-1)
            for nap in range(1, size+1):
                natrix = [matrix[i][k] for k in range(j-nap,j+nap+1)]
                if ispalindrome(natrix):
                    katrix = [matrix[p][j] for p in range(i-nap, i+nap+1)]
                    if ispalindrome(katrix):
                        count+=1
                    else:
                        break
                else:
                    break
    return(count+n*m)

def transpose(matrix):
    tatrix = []
    n = len(matrix)
    m = len(matrix[0])
    for i in range(m):
        row = []
        for j in range(n):
            row.append(matrix[j][i])
        tatrix.append(row)
    return tatrix    

START = time.time()
for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    matrix = []
    for _ in range(n):
        this = list(map(int, input().split()))
        matrix.append(this)
    ans = mana(matrix,n,m)
    if ans != 'FUCK':        
        print(ans)
    else:
        ans = oldie(matrix,n,m)
        print(ans)