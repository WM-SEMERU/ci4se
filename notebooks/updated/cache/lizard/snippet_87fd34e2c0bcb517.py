def get_tag_embs(self, tag_dims):
    return np.random.randn(self.tag_size, tag_dims).astype(np.float32)