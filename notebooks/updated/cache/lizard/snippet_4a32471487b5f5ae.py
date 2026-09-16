def remove_option(self, section, name, value=None):
    if self._is_live():
        raise RuntimeError('Submitted units cannot update their options')
    removed = 0
    for option in list(self._data['options']):
        if option['section'] == section:
            if option['name'] == name:
                if value is None or option['value'] == value:
                    self._data['options'].remove(option)
                    removed += 1
    if removed > 0:
        return True
    return False