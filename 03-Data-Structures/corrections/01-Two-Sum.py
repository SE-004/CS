# You are given an array of integers, nums, and an integer, target. Your goal is to find indices of two distinct elements in nums whose sum equals target. 
# You can’t use the same element twice, and you may return the indices in any order. You can assume there is exactly one valid solution for each input.
# Naive implementation (Time complexity O(n^2))
count1 = 0;
def two_sum(nums: list[int], target: int): 
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            count1+=1
            if nums[j] == target - nums[i]:
                return [i, j];

# print(two_sum([2,4,3,5,6], 5));

count2=0;
def two_sum_enumerate(nums: list[int], target: int): 
    n = len(nums)
    for i, num in enumerate(nums):
        for j, item in enumerate(nums):
            count2+=1
            if item == target - num:
                return [i, j];


# Hash table(python dictionary) implementation (Time complexity O(n))
def two_sum_hash(nums, target):
    hashmap = {};
    for i in range(len(nums)):
        complement = target - nums[i];
        if complement in hashmap:
            return [i, hashmap[complement]]
        hashmap[nums[i]] = i
    return []
    
print(two_sum_hash([2,4,3,5,6], 5));





