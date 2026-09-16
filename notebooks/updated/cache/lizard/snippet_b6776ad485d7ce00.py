def extract(self, path, extract_method, to_path):
    self._pbar_path.update_total(1)
    if extract_method not in _EXTRACT_METHODS:
        raise ValueError('Unknown extraction method "%s".' % extract_method)
    future = self._executor.submit(self._sync_extract, path, extract_method,
        to_path)
    return promise.Promise.resolve(future)