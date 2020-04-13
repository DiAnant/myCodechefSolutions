def nCr(n, k): 
    if(k > n - k): 
        k = n - k 
    res = 1
    for i in range(k): 
        res = res * (n - i) 
        res = res / (i + 1) 
    return res 
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    array =  list(map(int, input().split()))
    array.sort()
    saray = array[:k]
    freqs, freqa, mul = {}, {}, 1
    for i in list(set(saray)):
        freqs[i] = saray.count(i)
        freqa[i] = array.count(i)
    for i in list(set(saray)):
        mul = mul * nCr(freqa[i], freqs[i])
    print(int(mul))