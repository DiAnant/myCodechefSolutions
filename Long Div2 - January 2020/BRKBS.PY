for _ in range(int(input())):
    s,w1,w2,w3 = list(map(int, input().split()))
    hits = 0
    stack = [w1,w2,w3]
    if s >= sum(stack):
        print(1)
    elif s >= sum(stack[:2]) or s >= sum(stack[1:3]):
        print(2)
    else:
        print(3)
                