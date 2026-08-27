import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task08.unassisted import binary_search as bs_unassisted
from tasks.task08.assisted import binary_search as bs_assisted

@pytest.mark.parametrize("bs", [bs_unassisted, bs_assisted])
def test_binary_search(bs):
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert bs(arr, 7) == 3
    assert bs(arr, 1) == 0
    assert bs(arr, 15) == 7
    assert bs(arr, 8) == -1
    assert bs([], 5) == -1
