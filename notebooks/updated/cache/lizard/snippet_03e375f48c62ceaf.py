def interface_type(self):
    value = 'if='
    lst = self._attributes.get('if')
    if lst is None:
        value = ''
    else:
        value += '"' + str(lst) + '"'
    return value