def set_field(self, field, idx, value):
    if isinstance(idx, (int, float, str)):
        idx = [idx]
    if isinstance(value, (int, float)):
        value = [value]
    models = [self._idx_model[i] for i in idx]
    for i, m, v in zip(idx, models, value):
        assert hasattr(self.system.__dict__[m], field)
        uid = self.system.__dict__[m].get_uid(idx)
        self.system.__dict__[m].__dict__[field][uid] = v