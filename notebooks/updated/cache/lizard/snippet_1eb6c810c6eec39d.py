def option(self, key, value=None, **kwargs):
    if not isinstance(self._container, Section):
        raise ValueError('Options can only be added inside a section!')
    option = Option(key, value, container=self._container, **kwargs)
    option.value = value
    self._container.structure.insert(self._idx, option)
    self._idx += 1
    return self