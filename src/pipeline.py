from preprocessing import load_text, normalize, tokenize, remove_stopwords
from pattern_detection import detect_patterns
from statistic import word_frequencies, most_common_words, bigram_frequencies

def main():
    # Load and preprocess text data
    text = load_text("data/corpus.txt")
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    tokens = remove_stopwords(tokens)

    # Detect patterns in the text
    patterns = detect_patterns(normalized_text)

    # Calculate statistics on the tokens
    frequencies = word_frequencies(tokens)
    common_words = most_common_words(tokens)

    # Calculate bigram frequencies  
    bigram_freq = bigram_frequencies(tokens)
    top_bigrams = bigram_freq.most_common(10)

    # Print results
    print("Detected Patterns:", patterns)
    print("Word Frequencies:", frequencies)
    print("Most Common Words:", common_words)
    print("Bigram Frequencies:", bigram_freq)
    print("Top Bigrams:", top_bigrams)
    print("\n most common bigrams:")
    for bigram, freq in top_bigrams:
        print(f"{bigram}: {freq}")

    with open("results/output.txt", "w", encoding="utf-8") as f:
        f.write("Detected Patterns:\n")
        for pattern, count in patterns.items():
            f.write(f"{pattern}: {count}\n")
        f.write("\nMost Common Words:\n")
        for word, freq in common_words:
            f.write(f"{word}: {freq}\n")
        f.write("\nTop Bigrams:\n")
        for bigram, freq in top_bigrams:
            f.write(f"{bigram}: {freq}\n") 
        f.write("\nWord Frequencies:\n")
        for word, freq in frequencies.items():
            f.write(f"{word}: {freq}\n")
        f.write("\nBigram Frequencies:\n")
        for bigram, freq in bigram_freq.items():
            f.write(f"{bigram}: {freq}\n")
         

if __name__ == "__main__":
    main() 