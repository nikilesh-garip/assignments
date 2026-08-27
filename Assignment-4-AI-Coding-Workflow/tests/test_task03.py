import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task03.unassisted import find_palindromes as find_p_unassisted, longest_palindromic_substring as lps_unassisted
from tasks.task03.assisted import find_palindromes as find_p_assisted, longest_palindromic_substring as lps_assisted

@pytest.mark.parametrize("find_p, lps", [
    (find_p_unassisted, lps_unassisted),
    (find_p_assisted, lps_assisted)
])
def test_palindrome_detection(find_p, lps):
    text = "Madam saw a racecar at noon with radar"
    palindromes = find_p(text)
    assert "madam" in palindromes
    assert "racecar" in palindromes
    assert "noon" in palindromes
    assert "radar" in palindromes

    assert lps("babad") in ["bab", "aba"]
    assert lps("cbbd") == "bb"
    assert lps("") == ""
