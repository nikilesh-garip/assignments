"""
task01: User Validator (Unassisted implementation)
Validates email, password strength, and age requirements.
"""
import re

def validate_user(email: str, password: str, age: int) -> dict:
    errors = []
    
    # 1. Email check
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not email or not re.match(email_regex, email):
        errors.append("Invalid email format.")
        
    # 2. Password complexity
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one digit.")
    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter.")
    if not any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?" for c in password):
        errors.append("Password must contain at least one special character.")
        
    # 3. Age validation
    if age < 18:
        errors.append("User must be at least 18 years old.")
    elif age > 120:
        errors.append("Invalid age provided.")
        
    return {
        "is_valid": len(errors) == 0,
        "errors": errors
    }
