def stem_word(self, word):
    if self.is_plural(word):
        return self.stem_plural_word(word)
    else:
        return self.stem_singular_word(word)