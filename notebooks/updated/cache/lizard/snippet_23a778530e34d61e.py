def get(self, path, default=_NoDefault, as_type=None, resolve_references=True):
    value = self._source
    steps_taken = []
    try:
        for step in path.split(self._separator):
            steps_taken.append(step)
            value = value[step]
        if as_type:
            return as_type(value)
        elif isinstance(value, Mapping):
            namespace = type(self)(separator=self._separator, missing=self.
                _missing)
            namespace._source = value
            namespace._root = self._root
            return namespace
        elif resolve_references and isinstance(value, str):
            return self._resolve(value)
        else:
            return value
    except ConfiguredReferenceError:
        raise
    except KeyError as e:
        if default is not _NoDefault:
            return default
        else:
            missing_key = self._separator.join(steps_taken)
            raise NotConfiguredError('no configuration for key {}'.format(
                missing_key), key=missing_key) from e