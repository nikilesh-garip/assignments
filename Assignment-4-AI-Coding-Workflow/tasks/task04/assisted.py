"""
task04: Bank Transaction Balancer (AI-Assisted implementation)
Calculates running balances and detects overdraft events.
"""

def calculate_balance(transactions: list, initial_balance: float = 0.0) -> dict:
    balance = float(initial_balance)
    lowest = balance
    overdraft_events = 0
    
    for tx in transactions:
        balance += float(tx.get("amount", 0))
        if balance < 0:
            overdraft_events += 1
        if balance < lowest:
            lowest = balance
            
    return {
        "final_balance": round(balance, 2),
        "lowest_balance": round(lowest, 2),
        "overdraft_count": overdraft_events
    }
