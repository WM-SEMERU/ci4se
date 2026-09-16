def to_primitive(self, value, context=None):
    if context and context.get('rel_ids'):
        return value.rid
    else:
        return {'rtype': value.rtype, 'rid': value.rid}