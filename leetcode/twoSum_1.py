'''
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
        for index, num in enumerate(nums):
            try:
                index2 = -1
                index2 = nums.index(target-num)
                if index2 != -1 and index != index2:
                    return [index, index2]
            except:
                pass
        return []


class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return []
        defaultDict = {}
        for index, num in enumerate(nums):
            if num in defaultDict:
                return [defaultDict[num], index]
            else:
                defaultDict[target-num] = index
        return []
