def zipf_frequency(word, lang, wordlist='best', minimum=0.0):
    freq_min = zipf_to_freq(minimum)
    freq = word_frequency(word, lang, wordlist, freq_min)
    return round(freq_to_zipf(freq), 2)