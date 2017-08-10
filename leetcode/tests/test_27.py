'''
Usage:
    test removeElement_27.py by using pytest
'''
import pytest
import os
import sys
# append parent path
sys.path.append(os.path.pardir)
from removeElement_27 import Solution


test_data = [
    ([3, 2, 2, 3, 3, 4, 5, 6, 3], 3, [2, 2, 4, 5, 6]),
    ([2, 5, 8, 9, 10, 44], 8, [2, 5, 9, 10, 44]),
    ([1,1], 1, [])
]



@pytest.mark.parametrize("nums,val,expected", test_data)
def test_solution(nums, val, expected):
    cs = Solution()
    count = cs.removeElement(nums, val)
    assert nums[:count] == expected
