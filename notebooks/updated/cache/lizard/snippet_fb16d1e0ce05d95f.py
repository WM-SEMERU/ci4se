def read_keys(self, keys, dict_cls=AttrDict, path='/'):
    od = dict_cls()
    for k in keys:
        try:
            od[k] = self.read_value(k, path=path)
        except self.Error:
            try:
                od[k] = self.read_dimvalue(k, path=path)
            except self.Error:
                od[k] = None
    return od