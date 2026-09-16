def create_token_indices(self, tokens):
    start_index = len(self.special_token)
    indices = list(range(len(tokens) + start_index))
    tokens_with_special = self.special_token + list(tokens)
    self._token2idx = dict(list(zip(tokens_with_special, indices)))
    self._idx2token = dict(list(zip(indices, tokens_with_special)))