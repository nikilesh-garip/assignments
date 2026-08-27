"""
task01: User Validator (AI-Assisted implementation)
Validates email, password strength, and age requirements.
"""
import re

EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
SPECIAL_CHARS = set("!@#$%^&*()-_=+[]{}|;:,.<>?")

def validate_user(email: str, password: str, age: int) -> dict:
    errors = []
    
    if not email or not EMAIL_PATTERN.match(email):
        errors.append("Invalid email format.")
        
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not any(c.isdigit() for c in password):
        errors.append("Password must contain at least one digit.")
    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter.")
    if not any(c in SPECIAL_CHARS for c in password):
        errors.append("Password must contain at least one special character.")
        
    if not (18 <= age <= 120):
        errors.append("User must be at least 18 years old." if age < 18 else "Invalid age provided.")
        
    return {"is_valid": len(errors) == 0, "errors": errors}
