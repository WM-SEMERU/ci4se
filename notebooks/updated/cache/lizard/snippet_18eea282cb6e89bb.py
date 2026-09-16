def flatten(self, D):
    if not isinstance(D, dict):
        return D
    result = {}
    for k, v in D.items():
        if isinstance(v, dict):
            for _k, _v in self.flatten(v).items():
                result['.'.join([k, _k])] = _v
        else:
            result[k] = v
    return result