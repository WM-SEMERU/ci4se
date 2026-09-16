def _val_to_str(self, value):
    if isinstance(value, list):
        return ', '.join("'%s'" % str(i) for i in value)
    return str(value)