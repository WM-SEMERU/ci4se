def remove_object(self, name):
    if name not in self._object_map:
        raise RuntimeError('No object with name {} is registered.'.format(name)
            )
    for fn_name in list(self._function_map.keys()):
        if fn_name.startswith(name + '.') or fn_name.startswith(name + ':'):
            self._remove_function(fn_name)
    del self._object_map[name]