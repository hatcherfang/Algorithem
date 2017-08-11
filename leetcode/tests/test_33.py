'''
Usage:
    test searchInRSA_33.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from searchInRSA_33 import Solution


test_data = [
    ([5, 6, 0, 1, 2, 3, 4], 6, 1),
    ([1, 3, 5], 1, 0),
    ([1, 3, 5], 4, -1),
    ([6, 7, 1, 2, 3, 4, 5], 4, 5)
]



@pytest.mark.parametrize("nums,target,expected", test_data)
def test_solution(nums, target, expected):
    cs = Solution()
    assert cs.searchInRSA(nums, target) == expected

