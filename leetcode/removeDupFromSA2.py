'''
  80. Remove Duplicates from Sorted Array II
  Follow up for "Remove Duplicates":
  What if duplicates are allowed at most twice?

  For example,
  Given sorted array nums = [1,1,1,2,2,3],

  Your function should return length = 5, with the first five elements of nums
  being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new
  length.

  Author: hatcher fang
'''


def removeDupFromSortedArray2(nums):
    """
        :type nums: List[int]
        :rtype: int
    """
    if not nums:
        return
    if len(nums) <= 2:
        return len(nums)
    i = 2
    k = 2
    length = len(nums)
    while i < length:
        if nums[i] != nums[k-2]:
            nums[k] = nums[i]
            k = k + 1
        i = i + 1
    return k

if __name__ == '__main__':
    # nums = [1, 1, 1, 2, 2, 2, 3]
    # nums = [1, 1, 1]
    # nums = [1, 2, 2, 2]
    # nums = [1, 1, 2, 2]
    # nums = [-3, -1, 0, 0, 0, 3, 3]
    nums = [-3, 0, 0, 0, 0, 0, 0, 3, 3]
    print nums
    k = removeDupFromSortedArray2(nums)
    print nums[0:k]
