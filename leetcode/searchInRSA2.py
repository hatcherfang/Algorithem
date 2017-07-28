'''
    81. Search in Rotated Sorted Array II

    Follow up for "Search in Rotated Sorted Array":
    What if duplicates are allowed?

    Would this affect the run-time complexity? How and why?
    Suppose an array sorted in ascending order is rotated at some pivot unknown
    to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    Write a function to determine if a given target is in the array.

    The array may contain duplicates.

    Author: hatcher fang
'''


class Solution(object):
    def searchInRSA2(self, nums, target):
        """
           :type nums: List[int]
           :type target: int
           :rtype: bool
        """
        low = 0
        hight = len(nums) - 1
        while low <= hight:
            mid = (low+hight)/2
            if target == nums[mid]:
                return True
            else:
                print low, mid, hight
                if nums[low] < nums[mid]:
                    if nums[low] <= target and target < nums[mid]:
                        hight = mid - 1
                    else:
                        low = mid + 1
                    # mid = (low+hight)/2
                elif nums[low] > nums[mid]:
                    if nums[mid] < target and target <= nums[hight]:
                        low = mid + 1
                    else:
                        hight = mid - 1
                    # mid = (low+hight)/2
                else:
                    low = low + 1
        return False

if __name__ == '__main__':
    # nums = [5, 6, 0, 1, 2, 3, 4]
    # target = 6
    # nums = [1, 3, 1, 1, 1]
    # target = 3
    # nums = [1, 3]
    # target = 3
    nums = [1, 3, 5]
    target = 1
    cs = Solution()
    flag = cs.searchInRSA2(nums, target)
    print flag
