def get_pret_embs(self, word_dims=None):
    assert self._pret_embeddings is not None, 'No pretrained file provided.'
    pret_embeddings = gluonnlp.embedding.create(self._pret_embeddings[0],
        source=self._pret_embeddings[1])
    embs = [None] * len(self._id2word)
    for idx, vec in enumerate(pret_embeddings.idx_to_vec):
        embs[idx] = vec.asnumpy()
    if word_dims is None:
        word_dims = len(pret_embeddings.idx_to_vec[0])
    for idx, emb in enumerate(embs):
        if emb is None:
            embs[idx] = np.zeros(word_dims)
    pret_embs = np.array(embs, dtype=np.float32)
    return pret_embs / np.std(pret_embs)