'''
    27. Remove Element

    Given an array and a value, remove all instances of that value in place and
    return the new length.

    Do not allocate extra space for another array, you must do this in place
    with constant memory.

    The order of elements can be changed. It doesn't matter what you leave
    beyond the new length.

    Example:
    Given input array nums = [3,2,2,3], val = 3

    Your function should return length = 2, with the first two elements of nums
    being 2.
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # the most important thinking is two pointers
        if not nums:
            return 0
        length = len(nums)
        if not length:
            return 0
        i, j = 0, 0
        while j < length:
            if nums[j] != val:
                nums[i] = nums[j]
                i = i + 1
            j = j + 1
        return i
if __name__ == '__main__':
    cs = Solution()
    nums = [3, 2, 2, 3, 3, 4, 5, 6, 3]
    val = 3
    count = cs.removeElement(nums, val)
    print nums[:count]
