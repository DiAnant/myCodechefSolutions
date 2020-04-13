index = [None]*129
index[0] = 0
seq = [0]
for i in range(1,129):
    last = seq[-1]
    cunt = seq[:-1].count(last)
    if cunt == 0:
        seq.append(0)
        index[last] = i
    else:
        this = i - index[last]
        seq.append(this)
        index[last] = i
for _ in range(int(input())):
    n = int(input())
    ans = seq[:n].count(seq[:n][-1])
    print(ans)