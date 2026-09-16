def truncate_sentence(text, max_chars, break_words=False, padding=0):
    if break_words:
        return text[:-abs(max_chars - len(text)) - padding]
    words = []
    for word in text.split():
        predicted_len = sum(map(len, words)) + len(word) + len(words
            ) - 1 + padding
        if predicted_len >= max_chars:
            break
        words.append(word)
    return ' '.join(words)