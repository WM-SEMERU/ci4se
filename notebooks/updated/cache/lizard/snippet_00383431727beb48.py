def _words_plus_punc(self):
    no_punc_text = REGEX_REMOVE_PUNCTUATION.sub('', self.text)
    words_only = no_punc_text.split()
    words_only = set(w for w in words_only if len(w) > 1)
    punc_before = {''.join(p): p[1] for p in product(PUNC_LIST, words_only)}
    punc_after = {''.join(p): p[0] for p in product(words_only, PUNC_LIST)}
    words_punc_dict = punc_before
    words_punc_dict.update(punc_after)
    return words_punc_dict