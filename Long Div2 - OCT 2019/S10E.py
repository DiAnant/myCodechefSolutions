for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0
    for i, num in enumerate(nums):
        if i == 0:
            count += 1
        elif i < 5:
            if num < min(nums[:i]):
                count += 1
        else:
            if num < min(nums[i-5:i]):
                count += 1
    print(count)