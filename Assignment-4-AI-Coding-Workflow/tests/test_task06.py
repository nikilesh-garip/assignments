import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task06.unassisted import normalize_text as norm_unassisted
from tasks.task06.assisted import normalize_text as norm_assisted

@pytest.mark.parametrize("norm", [norm_unassisted, norm_assisted])
def test_string_normalization(norm):
    raw = "<p>Hello   “World” — welcome to ‘Python’  </p>"
    cleaned = norm(raw)
    assert cleaned == 'Hello "World" - welcome to \'Python\''
    assert norm("") == ""
