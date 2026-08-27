import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task01.unassisted import validate_user as validate_user_unassisted
from tasks.task01.assisted import validate_user as validate_user_assisted

@pytest.mark.parametrize("validator", [validate_user_unassisted, validate_user_assisted])
def test_user_validator_valid_case(validator):
    res = validator("test.user@example.com", "SecureP@ss123", 25)
    assert res["is_valid"] is True
    assert len(res["errors"]) == 0

@pytest.mark.parametrize("validator", [validate_user_unassisted, validate_user_assisted])
def test_user_validator_invalid_email(validator):
    res = validator("invalid_email", "SecureP@ss123", 25)
    assert res["is_valid"] is False
    assert any("email" in err.lower() for err in res["errors"])

@pytest.mark.parametrize("validator", [validate_user_unassisted, validate_user_assisted])
def test_user_validator_weak_password_and_underage(validator):
    res = validator("user@domain.com", "pass", 16)
    assert res["is_valid"] is False
    assert len(res["errors"]) >= 2
