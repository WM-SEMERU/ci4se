def set_config_item(self, key, value):
    try:
        old_value = self.get_config_item(key)
    except KeyError:
        old_value = None
    if isinstance(value, str):
        value = value.decode()
    elif isinstance(value, list):
        for i in range(len(value)):
            if isinstance(value[i], str):
                value[i] = value[i].decode()

    def set_key(key, value):
        self.clear_config_item(key)
        if isinstance(value, list):
            for entry in value:
                if not _lxc.Container.set_config_item(self, key, entry):
                    return False
        else:
            _lxc.Container.set_config_item(self, key, value)
    set_key(key, value)
    new_value = self.get_config_item(key)
    if key == 'lxc.loglevel':
        new_value = value
    if isinstance(value, unicode) and isinstance(new_value, unicode
        ) and value == new_value:
        return True
    elif isinstance(value, list) and isinstance(new_value, list) and set(value
        ) == set(new_value):
        return True
    elif isinstance(value, unicode) and isinstance(new_value, list) and set([
        value]) == set(new_value):
        return True
    elif old_value:
        set_key(key, old_value)
        return False
    else:
        self.clear_config_item(key)
        return False