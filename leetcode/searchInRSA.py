'''
    33. Search in Rotated Sorted Array
    Suppose an array sorted in ascending order is rotated at some pivot unknown
    to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return
    its index, otherwise return -1.

    You may assume no duplicate exists in the array.

    Author: hatcher fang
'''


def searchInRSA(nums, target):
    """
       :type nums: List[int]
       :type target: int
       :rtype: int
    """
    low = 0
    hight = len(nums) - 1
    while low <= hight:
        mid = (low+hight)/2
        print nums[mid], target
        if target == nums[mid]:
            return mid
        else:
            if nums[low] <= nums[mid]:
                if target < nums[mid] and target >= nums[low]:
                    hight = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[hight]:
                    low = mid + 1
                else:
                    hight = mid - 1
    return -1

if __name__ == '__main__':
    # nums = [5, 6, 0, 1, 2, 3, 4]
    # target = 6
    nums = [1, 3, 5]
    target = 1
    index = searchInRSA(nums, target)
    if index != -1:
        print index, nums[index]
