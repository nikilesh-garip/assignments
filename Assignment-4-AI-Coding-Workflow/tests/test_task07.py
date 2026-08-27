import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task07.unassisted import calculate_cart_total as cart_unassisted
from tasks.task07.assisted import calculate_cart_total as cart_assisted

@pytest.mark.parametrize("cart_calc", [cart_unassisted, cart_assisted])
def test_cart_calculation(cart_calc):
    items = [
        {"name": "Book", "price": 20.0, "qty": 2}, # 40
        {"name": "Pen", "price": 5.0, "qty": 4}    # 20 -> Subtotal = 60
    ]
    # 10% discount on 60 = 6, Taxable = 54, Tax @ 10% = 5.4, Final = 59.4
    res = cart_calc(items, discount_pct=10.0, tax_rate=0.10)
    assert res["subtotal"] == 60.0
    assert res["discount_amount"] == 6.0
    assert res["tax_amount"] == 5.4
    assert res["final_total"] == 59.4

@pytest.mark.parametrize("cart_calc", [cart_unassisted, cart_assisted])
def test_cart_negative_error(cart_calc):
    with pytest.raises(ValueError):
        cart_calc([{"name": "Bad", "price": -10.0, "qty": 1}])
