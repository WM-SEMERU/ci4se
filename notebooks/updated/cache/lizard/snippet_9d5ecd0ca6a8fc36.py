def from_dict(cls, d):
    return cls(d['rargname'], d['value'], list(d.get('properties', {}).
        items()), d.get('optional', False))