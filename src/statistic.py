from collections import Counter

# Statistical functions for text data
def word_frequencies(tokens):
    return Counter(tokens)

# Get the most common words in a list of tokens
def most_common_words(tokens, n=20):
    return Counter(tokens).most_common(n)

def generate_bigram(tokens):
    bigrams = []
    for i in range(len(tokens) - 1):
        bigrams.append((tokens[i], tokens[i + 1]))  # append a tuple of the current token and the next token
    return bigrams

def bigram_frequencies(tokens):
    bigrams = generate_bigram(tokens)
    return Counter(bigrams)