def tokenize(self, token_list):
    return [self._vocab_dict.get(token, self._vocab_dict[self.UNK]) for
        token in token_list]