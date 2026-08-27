"""
task04: Bank Transaction Balancer (Unassisted implementation)
Calculates running balances and detects overdraft events.
"""

def calculate_balance(transactions: list, initial_balance: float = 0.0) -> dict:
    balance = initial_balance
    lowest_balance = initial_balance
    overdraft_count = 0
    
    for tx in transactions:
        amount = tx.get("amount", 0.0)
        balance += amount
        if balance < 0:
            overdraft_count += 1
        if balance < lowest_balance:
            lowest_balance = balance
            
    return {
        "final_balance": round(balance, 2),
        "lowest_balance": round(lowest_balance, 2),
        "overdraft_count": overdraft_count
    }
