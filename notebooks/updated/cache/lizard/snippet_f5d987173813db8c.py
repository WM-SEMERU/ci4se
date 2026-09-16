def get_setting(self, key, converter=None, choices=None):
    value = self.addon.getSetting(id=key)
    if converter is str:
        return value
    elif converter is unicode:
        return value.decode('utf-8')
    elif converter is bool:
        return value == 'true'
    elif converter is int:
        return int(value)
    elif isinstance(choices, (list, tuple)):
        return choices[int(value)]
    elif converter is None:
        log.warning(
            'No converter provided, unicode should be used, but returning str value'
            )
        return value
    else:
        raise TypeError(
            'Acceptable converters are str, unicode, bool and int. Acceptable choices are instances of list  or tuple.'
            )