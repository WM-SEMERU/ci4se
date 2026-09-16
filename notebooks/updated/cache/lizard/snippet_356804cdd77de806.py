def make_result(self, result_class, node=None, prev_node=None, remember=
    True, key_chunks=None, notify=True, **kwargs):

    def canonicalize(node, **kwargs):
        return None if node is None else node.canonicalize(**kwargs)
    index = self.index
    result = result_class(canonicalize(node, **kwargs), canonicalize(
        prev_node, **kwargs), index)
    if not remember:
        return result
    self.history[index] = result_class(canonicalize(node, include_nodes=
        False), canonicalize(prev_node, include_nodes=False), index)
    key_chunks = key_chunks or split_key(node.key)
    asymptotic_key_chunks = (key_chunks[:x + 1] for x in xrange(len(
        key_chunks)))
    event_keys = [(False, key_chunks)]
    for _key_chunks in asymptotic_key_chunks:
        exact = _key_chunks == key_chunks
        self.indices.setdefault(_key_chunks, []).append((index, exact))
        event_keys.append((True, _key_chunks))
    if notify:
        for event_key in event_keys:
            try:
                event = self.events.pop(event_key)
            except KeyError:
                pass
            else:
                event.set()
    return result