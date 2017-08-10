'''
Usage:
    test twoSum_1.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from twoSum_1 import Solution
from twoSum_1 import Solution2


test_data = [
    ([2, 7, 11, 15], 13, [0, 2]),
    ([3, 2, 4], 6, [1, 2])
]


@pytest.mark.parametrize("nums,target,expected", test_data)
def test_solution(nums, target, expected):
    cs = Solution()
    assert cs.twoSum(nums, target) == expected
    cs2 = Solution2()
    assert cs2.twoSum(nums, target) == expected
