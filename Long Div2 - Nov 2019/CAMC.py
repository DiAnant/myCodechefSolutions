for _ in range(int(input())):
    n,m = list(map(int, input().split()))
    array = list(map(int, input().split()))
    korn = [[] for _ in range(m)]
    for i in range(n):
        korn[i%m].append(array[i])
    for i in korn:
        i.sort()
    pointers = [[0, len(korn[i])] for i in range(m)]
    ans = 1e30
    values = [korn[i][pointers[i][0]] for i in range(m)]
    nina = max(values)
    while(True):
        tina = min(values)
        diff = nina - tina
        if diff < ans:
            ans = diff
        mana = values.index(tina)
        pointers[mana][0] += 1
        if pointers[mana][0] >= pointers[mana][1]:
            break
        values[mana] = korn[mana][pointers[mana][0]]
        if values[mana] > nina:
            nina = values[mana]
    print(ans)