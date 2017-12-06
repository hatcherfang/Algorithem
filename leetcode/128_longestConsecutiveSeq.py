'''
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for num in nums:
            nums_dict[num] = False
        length = len(nums)
        longestLen = 0
        i = 0
        while i < length:
            if nums_dict[nums[i]]:
                i = i + 1
                continue
            v = nums[i]
            tmpLen = 1
            nums_dict[nums[i]] = True
            v1 = v + 1
            v2 = v - 1
            while True:
                if v1 in nums_dict and not nums_dict[v1]:
                    nums_dict[v1] = True
                    tmpLen = tmpLen + 1
                    v1 = v1 + 1
                else:
                    break
            while True:
                if v2 in nums_dict and not nums_dict[v2]:
                    nums_dict[v2] = True
                    tmpLen = tmpLen + 1
                    v2 = v2 - 1
                else:
                    break
            longestLen = max(longestLen, tmpLen)
            i = i + 1
        return longestLen


if __name__ == '__main__':
    cs = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print cs.longestConsecutive(nums)

