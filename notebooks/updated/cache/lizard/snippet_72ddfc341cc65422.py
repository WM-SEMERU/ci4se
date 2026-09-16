def plural_adj(self, text, count=None):
    pre, word, post = self.partition_word(text)
    if not word:
        return text
    plural = self.postprocess(word, self._pl_special_adjective(word, count) or
        word)
    return '{}{}{}'.format(pre, plural, post)