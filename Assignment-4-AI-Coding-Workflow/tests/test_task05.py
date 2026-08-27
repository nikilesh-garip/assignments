import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task05.unassisted import calculate_discount as disc_unassisted
from tasks.task05.assisted import calculate_discount as disc_assisted

@pytest.mark.parametrize("disc", [disc_unassisted, disc_assisted])
def test_store_discount_tiers(disc):
    # Platinum 20% on $200 = $40
    assert disc("platinum", 200.0) == 40.0
    # Gold 15% on $100 + SAVE10 ($10) = $25
    assert disc("gold", 100.0, coupon_code="SAVE10") == 25.0
    # Regular first order (5%) on $100 = $5
    assert disc("regular", 100.0, is_first_order=True) == 5.0
    # Zero cart total
    assert disc("platinum", 0.0) == 0.0
