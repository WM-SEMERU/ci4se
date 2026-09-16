def append(self, value, key=''):
    if type(value) in (list, tuple, dict):
        if type(value) == dict:
            for k in value.keys():
                self.append(value[k], k)
            return value.keys()
        keys = []
        for child in value:
            keys.append(self.append(child))
        return keys
    key = str(key)
    if not isinstance(value, Widget):
        raise ValueError(
            'value should be a Widget (otherwise use add_child(key,other)')
    if 'left' in value.style.keys():
        del value.style['left']
    if 'right' in value.style.keys():
        del value.style['right']
    if not 'order' in value.style.keys():
        value.style.update({'position': 'static', 'order': '-1'})
    if key.isdigit():
        value.style['order'] = key
    key = value.identifier if key == '' else key
    self.add_child(key, value)
    return key