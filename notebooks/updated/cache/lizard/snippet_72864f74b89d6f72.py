def _insert_pairs(self, ids_and_pairs):
    ids_to_insert = [x[0] for x in ids_and_pairs]
    for ids in self._key_ids.itervalues():
        for i, id in enumerate(ids):
            ids[i] += bisect(ids_to_insert, id)
    for i, pair in ids_and_pairs:
        self._pairs.insert(i, pair)