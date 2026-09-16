def diff(self, other):
    similar_param = {}
    different_param = {}
    for k1, v1 in self.items():
        if k1 not in other:
            different_param[k1] = {'INCAR1': v1, 'INCAR2': None}
        elif v1 != other[k1]:
            different_param[k1] = {'INCAR1': v1, 'INCAR2': other[k1]}
        else:
            similar_param[k1] = v1
    for k2, v2 in other.items():
        if k2 not in similar_param and k2 not in different_param:
            if k2 not in self:
                different_param[k2] = {'INCAR1': None, 'INCAR2': v2}
    return {'Same': similar_param, 'Different': different_param}