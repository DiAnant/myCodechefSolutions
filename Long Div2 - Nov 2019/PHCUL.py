def distance(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1] - c2[1])**2)**0.5

for _ in range(int(input())):
    home = tuple(list(map(int, input().split())))
    n, m, k = list(map(int, input().split()))
    ass = list(map(int, input().split()))
    ass = [(ass[i], ass[i+1]) for i in range(0, len(ass), 2)]
    bss = list(map(int, input().split()))
    bss = [(bss[i], bss[i+1]) for i in range(0, len(bss), 2)]
    css = list(map(int, input().split()))
    css = [(css[i], css[i+1]) for i in range(0, len(css), 2)]
    # input taken.

    pos = 1e50
    for a in ass:
        gk1 = distance(home, a)
        if gk1 > pos:
            continue
        for b in bss:
            gk2 = distance(a,b)
            if gk1 + gk2 > pos:
                continue
            for c in css:
                x = gk1 + gk2 + distance(b, c)
                pos = min(x, pos)

    for b in bss:
        gk1 = distance(home, b)
        if gk1 > pos:
            continue
        for a in ass:
            gk2 = distance(b, a)
            if gk1 + gk2 > pos:
                continue
            for c in css:
                x = gk1 + gk2 + distance(a, c)
                pos = min(x, pos)

    print(pos)