def remove(self, arr):
    name = arr if isinstance(arr, six.string_types) else arr.psy.arr_name
    if arr not in self:
        raise ValueError('Array {0} not in the list'.format(name))
    for i, arr in enumerate(self):
        if arr.psy.arr_name == name:
            del self[i]
            return
    raise ValueError('No array found with name {0}'.format(name))