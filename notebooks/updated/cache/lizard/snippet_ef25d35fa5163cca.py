def load(self, path: str, k: Optional[int]=None):
    load_time_start = time.time()
    with open(path, 'rb') as inp:
        _lex = np.load(inp)
    loaded_k = _lex.shape[1]
    if k is not None:
        top_k = min(k, loaded_k)
        if k > loaded_k:
            logger.warning(
                'Can not load top-%d translations from lexicon that contains at most %d entries per source.'
                , k, loaded_k)
    else:
        top_k = loaded_k
    self.lex = np.zeros((len(self.vocab_source), top_k), dtype=_lex.dtype)
    for src_id, trg_ids in enumerate(_lex):
        self.lex[(src_id), :] = np.sort(trg_ids[:top_k])
    load_time = time.time() - load_time_start
    logger.info('Loaded top-%d lexicon from "%s" in %.4fs.', top_k, path,
        load_time)