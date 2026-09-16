def _pk(self, obj):
    pk_values = tuple(getattr(obj, c.name) for c in obj.__mapper__.primary_key)
    if len(pk_values) == 1:
        return pk_values[0]
    return pk_values