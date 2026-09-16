def _getter(self):

    def get_attr_value(obj):
        attr_str_value = obj.get(self._clark_name)
        if attr_str_value is None:
            return self._default
        return self._simple_type.from_xml(attr_str_value)
    get_attr_value.__doc__ = self._docstring
    return get_attr_value