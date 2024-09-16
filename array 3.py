def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1
nums=[2, 1, 3, 5, 3, 2]
nums=[1,2,3,4,5]
print(first_duplicate(nums))
