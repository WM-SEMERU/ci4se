def basic_word_sim(word1, word2):
    return sum([(1) for c in word1 if c in word2]) / max(len(word1), len(word2)
        )