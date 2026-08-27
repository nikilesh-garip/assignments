"""
task05: Store Discount Calculator (AI-Assisted Refactored implementation)
Refactored dictionary-driven discount calculator.
"""

TIER_RATES = {"platinum": 0.20, "gold": 0.15, "silver": 0.10, "regular": 0.0}
COUPONS = {"SAVE10": 10.0, "SAVE20": 20.0, "WELCOME5": 5.0}

def calculate_discount(customer_type: str, cart_total: float, is_first_order: bool = False, coupon_code: str = None) -> float:
    if cart_total <= 0:
        return 0.0
        
    tier_rate = TIER_RATES.get(customer_type.lower(), 0.0)
    if is_first_order and tier_rate == 0.0:
        tier_rate = 0.05
        
    total_discount = (cart_total * tier_rate) + COUPONS.get((coupon_code or "").upper(), 0.0)
    return min(round(total_discount, 2), float(cart_total))
