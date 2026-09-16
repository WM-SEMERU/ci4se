def get_precomposed_chars():
    return set([letter for letter in chart.consonants if unicodedata.
        normalize('NFD', letter) != letter])