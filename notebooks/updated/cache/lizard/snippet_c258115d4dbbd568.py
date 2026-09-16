def compare(self, word1, word2):
    return self._plequal(word1, word2, self.plural_noun) or self._plequal(word1
        , word2, self.plural_verb) or self._plequal(word1, word2, self.
        plural_adj)