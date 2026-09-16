def _get_next(self, history):
    orig_history = history
    if not history:
        return helper.START
    history = history[-(self._n - 1):]
    while history and not self._T.get(history):
        history = history[1:]
    kv = [(k, v) for k, v in self._T.items(history) if not (k in
        reserved_words or k == history)]
    total = sum(v for k, v in kv)
    while total == 0 and len(history) > 0:
        history = history[1:]
        kv = [(k, v) for k, v in self._T.items(history) if not (k in
            reserved_words or k == history)]
        total = sum(v for k, v in kv)
    assert total > 0, 'Sorry there is no n-gram with {!r}'.format(orig_history)
    d = defaultdict(float)
    total = self._T.get(history)
    for k, v in kv:
        k = k[len(history):]
        d[k] += (v + 1) / (total + N_VALID_CHARS - 1)
    return d