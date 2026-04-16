import re

# Preprocessing functions for text data
def load_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
# Normalization functions for text data
def normalize(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text

# Tokenization functions for text data
def tokenize(text):
    tokens = re.findall(r"\b\w+\b", text)  # Match words (alphanumeric sequences)
    tokens = [token for token in tokens if len(token) > 1]
    return tokens

STOPWORDS = {
    "der", "die", "das", "und", "er", "sie", "es", "zu", "in", "den", "dem",
    "ein", "eine", "nicht", "mit", "sich", "ich", "auf", "von", "ist", "war"
}

def remove_stopwords(tokens):
    return [token for token in tokens if token not in STOPWORDS]