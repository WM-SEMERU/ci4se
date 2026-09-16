def substitute(self, var_map):
    if self in var_map:
        return var_map[self]
    return self._substitute(var_map)