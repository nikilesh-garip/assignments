"""
task03: Palindrome Finder (AI-Assisted implementation)
Finds palindrome words and longest palindromic substring using expand around center.
"""
import re

def find_palindromes(text: str) -> list:
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return [w for w in words if len(w) > 1 and w == w[::-1]]

def longest_palindromic_substring(s: str) -> str:
    if not s:
        return ""
        
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        p1 = expand(i, i)       # Odd length
        p2 = expand(i, i + 1)   # Even length
        if len(p1) > len(longest):
            longest = p1
        if len(p2) > len(longest):
            longest = p2
            
    return longest
