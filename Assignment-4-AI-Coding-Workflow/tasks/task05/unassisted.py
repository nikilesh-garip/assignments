"""
task05: Store Discount Calculator (Unassisted Refactored implementation)
Clean rules-based discount calculator.
"""

TIER_DISCOUNTS = {
    "platinum": 0.20,
    "gold": 0.15,
    "silver": 0.10,
    "regular": 0.00
}

COUPON_DISCOUNTS = {
    "SAVE10": 10.0,
    "SAVE20": 20.0,
    "WELCOME5": 5.0
}

def calculate_discount(customer_type: str, cart_total: float, is_first_order: bool = False, coupon_code: str = None) -> float:
    if cart_total <= 0:
        return 0.0
        
    rate = TIER_DISCOUNTS.get(customer_type.lower(), 0.0)
    if is_first_order and customer_type.lower() == "regular":
        rate = max(rate, 0.05)
        
    discount = cart_total * rate
    
    if coupon_code and coupon_code.upper() in COUPON_DISCOUNTS:
        discount += COUPON_DISCOUNTS[coupon_code.upper()]
        
    return min(round(discount, 2), cart_total)
