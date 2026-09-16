def apply(self, word, ctx=None):
    return Sequential.in_sequence(word, AdjacentVowels.uyir_letters,
        AdjacentVowels.reason)