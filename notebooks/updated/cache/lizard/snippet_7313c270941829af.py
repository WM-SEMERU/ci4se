def ngram_count(text, N=1, keep_punct=False):
    if not keep_punct:
        text = re.sub('[^A-Z]', '', text.upper())
    count = {}
    for i in range(len(text) - N + 1):
        c = text[i:i + N]
        if c in count:
            count[c] += 1
        else:
            count[c] = 1.0
    return count