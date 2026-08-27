"""
task03: Palindrome Finder (Unassisted implementation)
Finds palindrome words and longest palindromic substring.
"""
import re

def find_palindromes(text: str) -> list:
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return [w for w in words if len(w) > 1 and w == w[::-1]]

def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j+1]
            if sub == sub[::-1] and len(sub) > len(longest):
                longest = sub
    return longest
