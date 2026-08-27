"""
task06: String Normalizer (Unassisted implementation)
Cleans extra spaces, normalizes quotes/dashes, and strips HTML tags.
"""
import re

def normalize_text(raw_text: str) -> str:
    if not raw_text:
        return ""
    # Strip HTML tags
    text = re.sub(r'<[^>]+>', '', raw_text)
    # Normalize unicode quotes and dashes
    text = text.replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")
    text = text.replace('—', '-').replace('–', '-')
    # Collapse multiple whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()
