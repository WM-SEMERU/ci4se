def _merge_a_into_b(self, a, b):
    from easydict import EasyDict as edict
    if type(a) is not edict:
        return
    for k, v in a.items():
        if k not in b:
            raise KeyError('{} is not a valid config key'.format(k))
        old_type = type(b[k])
        if old_type is not type(v):
            if isinstance(b[k], np.ndarray):
                v = np.array(v, dtype=b[k].dtype)
            else:
                raise ValueError('Type mismatch ({} vs. {}) for config key: {}'
                    .format(type(b[k]), type(v), k))
        if type(v) is edict:
            try:
                self._merge_a_into_b(a[k], b[k])
            except:
                print('Error under config key: {}'.format(k))
                raise
        else:
            b[k] = v
    return b