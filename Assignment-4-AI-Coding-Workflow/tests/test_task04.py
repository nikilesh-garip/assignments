import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task04.unassisted import calculate_balance as calc_unassisted
from tasks.task04.assisted import calculate_balance as calc_assisted

@pytest.mark.parametrize("calc", [calc_unassisted, calc_assisted])
def test_bank_transactions_normal(calc):
    txs = [
        {"amount": 100.0},
        {"amount": -30.0},
        {"amount": 50.0},
        {"amount": -20.0}
    ]
    res = calc(txs, initial_balance=50.0)
    assert res["final_balance"] == 150.0
    assert res["overdraft_count"] == 0
    assert res["lowest_balance"] == 50.0

@pytest.mark.parametrize("calc", [calc_unassisted, calc_assisted])
def test_bank_transactions_overdraft(calc):
    txs = [
        {"amount": -100.0},
        {"amount": 50.0},
        {"amount": -80.0}
    ]
    res = calc(txs, initial_balance=20.0)
    assert res["final_balance"] == -110.0
    assert res["overdraft_count"] == 3
    assert res["lowest_balance"] == -110.0
