'''
Usage:
    test removeDupFromSA_26.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from removeDupFromSA_26 import Solution


test_data = [
    ([1, 1, 2, 2, 2, 3, 4, 4, 6, 7, 9], [1, 2, 3, 4, 6, 7, 9]),
    ([4, 4, 4, 5, 5, 6, 9, 1, 1, 0, 0], [4, 5, 6, 9, 1, 0]),
    ([1, 1, 2, 2], [1, 2])
]


@pytest.mark.parametrize("nums,expected", test_data)
def test_solution(nums, expected):
    cs = Solution()
    k = cs.removeDupFromSortedArray(nums)
    assert nums[0:k] == expected
