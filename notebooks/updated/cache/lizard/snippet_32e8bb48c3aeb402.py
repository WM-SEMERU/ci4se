def save(self, name, data, location='local', kind='json'):
    file_ext = '.json' if kind == 'json' else '.pkl'
    path = self._get_path(name, location, file_ext=file_ext)
    _ensure_dir_exists(op.dirname(path))
    logger.debug('Save data to `%s`.', path)
    if kind == 'json':
        _save_json(path, data)
    else:
        _save_pickle(path, data)