def _collection(self):
    old_sort_limits_and_len_mode = (None if self._sort_limits is None else
        self._sort_limits.copy(), self._len_mode)
    try:
        conn = self.cls.get_connection()
        self._len = 0
        try:
            pk = self._get_pk()
        except ValueError:
            return []
        else:
            if pk is not None and not self.cls.get_field('pk').exists(pk):
                return []
        sort_options = self._prepare_sort_options(bool(pk))
        final_set, keys_to_delete = self._get_final_set(self.
            _lazy_collection['sets'], pk, sort_options)
        if self._len_mode:
            if final_set is None:
                if pk and not self._lazy_collection['sets']:
                    self._len = 1
                else:
                    self._len = 0
            else:
                self._len = self._collection_length(final_set)
                if keys_to_delete:
                    conn.delete(*keys_to_delete)
            return
        else:
            if final_set is None:
                if pk and not self._lazy_collection['sets']:
                    collection = {pk}
                else:
                    collection = {}
            else:
                collection = self._final_redis_call(final_set, sort_options)
                if keys_to_delete:
                    conn.delete(*keys_to_delete)
            return self._prepare_results(collection)
    finally:
        self._sort_limits, self._len_mode = old_sort_limits_and_len_mode