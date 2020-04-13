def magic(array):
    n = len(array)
    for i in range(0, n - 1):
        if array[i] == 0 and array[i+1] == 0:
            return False
    if n < 3:
        return True
    for i in range(0, n - 2):
        if array[i] ==0 and array[i+1] == 1 and array[i+2] == 0:
            return False
    return True
    

for _ in range(int(input().strip())):
    n = int(input().strip())
    alice, bob = 0, 0
    alice_occur = [0]*26
    alice_words = [0]*26
    bob_occur = [0]*26
    bob_words = [0]*26
    for _ in range(n):
        string = input().strip()
        array = [0]*len(string)
        inwhich = [0]*26
        for ind, i in enumerate(string):
            inwhich[ord(i)-97] += 1
            if i == 'a' or i =='e' or i =='i' or i=='o' or i == 'u':
                array[ind] = 1
        if magic(array)==True:
            # alice wins
            alice += 1
            for j in range(len(inwhich)):
                if inwhich[j] > 0:
                    alice_words[j] += 1
                alice_occur[j] += inwhich[j]
        else:
            # bob wins this round
            bob += 1
            for j in range(len(inwhich)):
                if inwhich[j] > 0:
                    bob_words[j] += 1
                bob_occur[j] += inwhich[j]
    
    aloc, boboc, alwo, bowo = 1,1,1,1
    for i in range(26):
        x = bob_occur[i]
        if x != 0:
            y = bob_words[i]
            boboc = boboc * x
            bowo = bowo * y
            
        x = alice_occur[i]
        if x != 0:
            y = alice_words[i]
            aloc = aloc * x
            alwo = alwo * y

#     try:
    ratio = alwo / bowo
    if bob > alice:
        ratio = ratio * ((boboc/aloc)**alice) * (bobob**(bob-alice))
    else:
        ratio = ratio * ((boboc/aloc)**bob) * ((1/aloc)**(alice-bob))

    if ratio > 1e7:
        print('Infinity')
    else:
        print(ratio)
#     except ZeroDivisionError:
#         print('Infinity')