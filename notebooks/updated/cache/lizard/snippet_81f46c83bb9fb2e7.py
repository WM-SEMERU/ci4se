def component(self, **kwargs):
    kwargs_copy = self.base_dict.copy()
    kwargs_copy.update(**kwargs)
    self._replace_none(kwargs_copy)
    try:
        return NameFactory.component_format.format(**kwargs_copy)
    except KeyError:
        return None