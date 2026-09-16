def import_model(self, name, path='floyd.db.models'):
    if name in self._model_cache:
        return self._model_cache[name]
    try:
        model = getattr(__import__(path, None, None, [name]), name)
        self._model_cache[name] = model
    except ImportError:
        return False
    return model