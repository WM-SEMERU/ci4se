def istring(self, in_string=''):
    new_string = IString(in_string)
    new_string.set_std(self.features.get('casemapping'))
    if not self._casemap_set:
        self._imaps.append(new_string)
    return new_string