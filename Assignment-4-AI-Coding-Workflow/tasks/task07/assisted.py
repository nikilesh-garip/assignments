"""
task07: Shopping Cart Price Calculator (AI-Assisted implementation)
Calculates cart subtotal, discount deductions, tax, and final amount.
"""

def calculate_cart_total(items: list, discount_pct: float = 0.0, tax_rate: float = 0.08) -> dict:
    subtotal = 0.0
    for item in items:
        p, q = item.get("price", 0.0), item.get("qty", 1)
        if p < 0 or q < 0:
            raise ValueError("Price and quantity must be non-negative.")
        subtotal += p * q
        
    discount = round(subtotal * (discount_pct / 100.0), 2)
    taxable = subtotal - discount
    tax = round(taxable * tax_rate, 2)
    return {
        "subtotal": round(subtotal, 2),
        "discount_amount": discount,
        "tax_amount": tax,
        "final_total": round(taxable + tax, 2)
    }
