def transcribe(self, text, as_phonemes=False):
    phoneme_words = [self.transcribe_word(word) for word in self._tokenize(
        text)]
    if not as_phonemes:
        words = [''.join([phoneme.ipa for phoneme in word]) for word in
            phoneme_words]
        return ' '.join(words)
    else:
        return phoneme_words