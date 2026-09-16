def all(self, **kwargs):
    if self._is_transposed:
        kwargs['bool_only'] = False
        kwargs['axis'] = kwargs.get('axis', 0) ^ 1
        return self.transpose().all(**kwargs)
    return self._process_all_any(lambda df, **kwargs: df.all(**kwargs), **
        kwargs)