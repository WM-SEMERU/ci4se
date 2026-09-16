def _append_object(self, value, _file):
    _labs = ' {'
    _file.write(_labs)
    self._tctr += 1
    for _item, _text in value.items():
        _tabs = '\t' * self._tctr
        _cmma = ',' if self._vctr[self._tctr] else ''
        _keys = '{cmma}\n{tabs}"{item}" :'.format(cmma=_cmma, tabs=_tabs,
            item=_item)
        _file.write(_keys)
        self._vctr[self._tctr] += 1
        _text = self.object_hook(_text)
        _type = type(_text).__name__
        _MAGIC_TYPES[_type](self, _text, _file)
    self._vctr[self._tctr] = 0
    self._tctr -= 1
    _tabs = '\t' * self._tctr
    _labs = '\n{tabs}{}'.format('}', tabs=_tabs)
    _file.write(_labs)