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

