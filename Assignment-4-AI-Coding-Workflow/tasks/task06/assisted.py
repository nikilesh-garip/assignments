"""
task06: String Normalizer (AI-Assisted implementation)
Cleans extra spaces, normalizes quotes/dashes, and strips HTML tags.
"""
import re

HTML_TAG_REGEX = re.compile(r"<[^>]+>")
WHITESPACE_REGEX = re.compile(r"\s+")
CHAR_MAP = str.maketrans({
    "“": '"', "”": '"', "‘": "'", "’": "'",
    "—": "-", "–": "-"
})

def normalize_text(raw_text: str) -> str:
    if not raw_text:
        return ""
    no_html = HTML_TAG_REGEX.sub("", raw_text)
    normalized_chars = no_html.translate(CHAR_MAP)
    return WHITESPACE_REGEX.sub(" ", normalized_chars).strip()
