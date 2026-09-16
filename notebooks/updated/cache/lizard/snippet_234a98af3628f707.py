def attribute_requirement(self, entity_id, index=None):
    res = {'required': [], 'optional': []}
    try:
        for sp in self[entity_id]['spsso_descriptor']:
            _res = attribute_requirement(sp, index)
            res['required'].extend(_res['required'])
            res['optional'].extend(_res['optional'])
    except KeyError:
        return None
    return res