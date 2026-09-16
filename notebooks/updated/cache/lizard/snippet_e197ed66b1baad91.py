def set_num_special_tokens(self, num_special_tokens):
    self.transformer.set_num_special_tokens(num_special_tokens)
    self.lm_head.set_embeddings_weights(self.transformer.tokens_embed.weight)