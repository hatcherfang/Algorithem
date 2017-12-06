'''
Usage:
    test longestConsecutiveSeq_128.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from longestConsecutiveSeq_128 import Solution


test_data = [
    ([100, 4, 200, 1, 3, 2], 4),
    ([4, 5, 3, 1], 3),
    ([1, 2, 3, 4], 4),
    ([1, 1, 1], 1)
]


@pytest.mark.parametrize("nums,expected", test_data)
def test_solution(nums, expected):
    cs = Solution()
    assert cs.longestConsecutive(nums) ==  expected

