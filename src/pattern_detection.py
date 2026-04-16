import re;  # Regular expressions for pattern detection

# Pattern detection functions for text data
def detect_patterns(text):
    
    patterns = {
        "dass_clause": r"\b(dass|daß)\b",
        "modal_verbs": r"\b(kann|muss|muß|soll|will)\b"
    }

    detected_patterns = {}

    for pattern_name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        detected_patterns[pattern_name] = len(matches)
    
    return detected_patterns