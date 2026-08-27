"""
task07: Shopping Cart Price Calculator (Unassisted implementation)
Calculates cart subtotal, discount deductions, tax, and final amount.
"""

def calculate_cart_total(items: list, discount_pct: float = 0.0, tax_rate: float = 0.08) -> dict:
    subtotal = 0.0
    for item in items:
        price = item.get("price", 0.0)
        qty = item.get("qty", 1)
        if price < 0 or qty < 0:
            raise ValueError("Price and quantity must be non-negative.")
        subtotal += price * qty
        
    discount_amount = round(subtotal * (discount_pct / 100.0), 2)
    discounted_subtotal = max(0.0, subtotal - discount_amount)
    tax_amount = round(discounted_subtotal * tax_rate, 2)
    final_total = round(discounted_subtotal + tax_amount, 2)
    
    return {
        "subtotal": round(subtotal, 2),
        "discount_amount": discount_amount,
        "tax_amount": tax_amount,
        "final_total": final_total
    }
