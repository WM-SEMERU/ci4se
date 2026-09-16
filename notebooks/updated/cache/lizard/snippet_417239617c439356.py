def _Open(self, path_spec=None, mode='rb'):
    if not path_spec:
        raise ValueError('Missing path specification.')
    if path_spec.HasParent():
        raise errors.PathSpecError(
            'Unsupported path specification with parent.')
    location = getattr(path_spec, 'location', None)
    if location is None:
        raise errors.PathSpecError('Path specification missing location.')
    self._current_offset = 0
    self._size = len(self._file_data)