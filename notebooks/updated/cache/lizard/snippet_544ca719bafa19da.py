def spellcheck_results(self):
    if not self.is_tagged(WORDS):
        self.tokenize_words()
    return vabamorf.spellcheck(self.word_texts, suggestions=True)