def field2default(self, field):
    ret = {}
    if 'doc_default' in field.metadata:
        ret['default'] = field.metadata['doc_default']
    else:
        default = field.missing
        if default is not marshmallow.missing and not callable(default):
            ret['default'] = default
    return ret