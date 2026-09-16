def _get_final_set(self, sets, pk, sort_options):
    conn = self.cls.get_connection()
    all_sets = set()
    tmp_keys = set()
    if pk is not None and not sets and not (sort_options and sort_options.
        get('get')):
        return None, False
    elif sets or pk:
        if sets:
            new_sets, new_tmp_keys = self._prepare_sets(sets)
            all_sets.update(new_sets)
            tmp_keys.update(new_tmp_keys)
        if pk is not None:
            tmp_key = self._unique_key()
            conn.sadd(tmp_key, pk)
            all_sets.add(tmp_key)
            tmp_keys.add(tmp_key)
    else:
        all_sets.add(self.cls.get_field('pk').collection_key)
    if not all_sets:
        delete_set_later = False
        final_set = None
    elif len(all_sets) == 1:
        final_set = all_sets.pop()
        if final_set in tmp_keys:
            delete_set_later = True
            tmp_keys.remove(final_set)
        else:
            delete_set_later = False
    else:
        delete_set_later = True
        final_set = self._combine_sets(all_sets, self._unique_key())
    if tmp_keys:
        conn.delete(*tmp_keys)
    return final_set, [final_set] if delete_set_later else None