'''
Usage:
    test removeDupFromSA2_80.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from removeDupFromSA2_80 import Solution


test_data = [
    ([1, 1, 1, 2, 2, 2, 3], [1, 1, 2, 2, 3]),
    ([1, 1, 1], [1, 1]),
    ([1, 2, 2, 2], [1, 2, 2]),
    ([-3, -1, 0, 0, 0, 3, 3], [-3, -1, 0, 0, 3, 3])
]


@pytest.mark.parametrize("nums,expected", test_data)
def test_solution(nums, expected):
    cs = Solution()
    k = cs.removeDupFromSortedArray2(nums)
    assert nums[0:k] == expected
