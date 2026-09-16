def ngram_freq(text, N=1, log=False, floor=0.01):
    freq = ngram_count(text, N)
    L = 1.0 * (len(text) - N + 1)
    for c in freq.keys():
        if log:
            freq[c] = math.log10(freq[c] / L)
        else:
            freq[c] = freq[c] / L
    if log:
        freq['floor'] = math.log10(floor / L)
    else:
        freq['floor'] = floor / L
    return freq