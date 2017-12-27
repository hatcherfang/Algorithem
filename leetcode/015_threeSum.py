'''
15. 3Sum

Given an array S of n integers, are there elements a, b, c in S such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        sorted_nums = sorted(nums)
        left, right = 0, len(sorted_nums)-1
        result = []
        while left <= right-2:
            if 0 < left <= right-2 and sorted_nums[left-1] == sorted_nums[left]:
                left = left + 1
                continue
            low = left
            mid = left + 1
            high = right
            while mid < high:
                target = sorted_nums[low] + sorted_nums[mid] + sorted_nums[high]
                if target < 0:
                    mid = mid + 1
                elif target > 0:
                    high = high - 1
                else:
                    result.append([sorted_nums[low], sorted_nums[mid],
                                  sorted_nums[high]])
                    while mid < high and sorted_nums[mid] == sorted_nums[mid+1]:
                        mid = mid + 1
                    while mid < high and sorted_nums[high] == sorted_nums[high-1]:
                        high = high - 1
                    mid = mid + 1
                    high = high - 1
            left = left + 1
        return result

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    cs = Solution()
    print cs.threeSum(nums)


