# LeetCode Problem: Two Sum
# problem link : https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

#solution 1 , this solution has a time complexity of O(N^2) in the worst-case scenario. 
#This inefficiency arises because the in operator and index method, used within the loop, 
# both iterate through the list, potentially leading to quadratic time complexity.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for x in range(l):
            y = target - nums[x]
            if y in nums and x != nums.index(y):
                if x < nums.index(y):
                    return [x, nums.index(y)]
                else:
                    return [nums.index(y), x]

# Solution 2
# This solution improves upon the brute force approach by utilizing a hash table to store 
# the numbers and their indices as they are processed. This allows the function to 
# check if the complement of the current number (i.e., target - current number) exists 
# in the table as it iterates through the array. If it exists, it immediately returns 
# the indices of the current number and its complement, achieving a time complexity 
# of O(N), where N is the number of elements in the input array.
#
# Key Steps:
# 1. Iterate over each element in the array.
# 2. Calculate the complement by subtracting the current element value from the target.
# 3. Check if the complement exists in the hash table:
#    - If it does, return the indices of the complement and the current element.
#    - If it doesn't, add the current element and its index to the hash table.
# This ensures that each element is processed only once, making the function efficient 
# and fast for large arrays.

class Solution:
    def twoSum(self, nums, target):
        num_set = {}
        for num_index, num in enumerate(nums):
            if (target-num) in num_set:
                return [num_set[target-num], num_index]
            num_set[num] = num_index
