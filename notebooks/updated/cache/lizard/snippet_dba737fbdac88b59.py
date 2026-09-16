def merge(var1, var2):
    out = {}
    out['value'] = var2.get('value', var1.get('value', None))
    out['mimetype'] = var2.get('mimetype', var1.get('mimetype', None))
    out['types'] = var2.get('types') + [x for x in var1.get('types') if x
         not in var2.get('types')]
    out['optional'] = var2.get('optional', var1.get('optional', False))
    out['filename'] = var2.get('filename', var2.get('filename', None))
    return Variable(var1.default_type, **out)