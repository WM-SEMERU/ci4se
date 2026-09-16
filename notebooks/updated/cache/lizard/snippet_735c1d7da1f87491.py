def maximum_size_estimated(self):
    value = 'sz='
    lst = self._attributes.get('sz')
    if lst is None:
        value = ''
    else:
        value += '"' + str(lst) + '"'
    return value