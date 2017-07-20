'''
    26. Remove Duplicates from Sorted Array

    Given a sorted array, remove the duplicates in place such that each element
    appear only once and return the new length.

    Do not allocate extra space for another array, you must do this in place
    with constant memory.

    For example,
    Given input array nums = [1,1,2],

    Your function should return length = 2, with the first two elements of nums
    being 1 and 2 respectively. It doesn't matter what you leave beyond the new
    length.
    Author: hatcher fang
'''


def removeDupFromSortedArray(nums):
    """
        :type nums: List[int]
        :rtype: int
    """
    if not nums:
        return
    i = 1
    k = 0
    length = len(nums)
    while i < length:
        if nums[i] != nums[k]:
            k = k + 1
            nums[k] = nums[i]
        i = i + 1
    return k+1

if __name__ == '__main__':
    L = [1, 1, 2, 2, 2, 3, 4, 4, 6, 7, 9]
    k = removeDupFromSortedArray(L)
    print L[0:k]
