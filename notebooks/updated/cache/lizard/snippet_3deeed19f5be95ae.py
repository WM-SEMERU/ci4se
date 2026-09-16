def default(self, o):
    if isinstance(o, datetime.datetime):
        return {'@module': 'datetime', '@class': 'datetime', 'string': o.
            __str__()}
    if np is not None:
        if isinstance(o, np.ndarray):
            return {'@module': 'numpy', '@class': 'array', 'dtype': o.dtype
                .__str__(), 'data': o.tolist()}
        elif isinstance(o, np.generic):
            return o.item()
    if bson is not None:
        if isinstance(o, bson.objectid.ObjectId):
            return {'@module': 'bson.objectid', '@class': 'ObjectId', 'oid':
                str(o)}
    try:
        d = o.as_dict()
        if '@module' not in d:
            d['@module'] = '{}'.format(o.__class__.__module__)
        if '@class' not in d:
            d['@class'] = '{}'.format(o.__class__.__name__)
        if '@version' not in d:
            try:
                parent_module = o.__class__.__module__.split('.')[0]
                module_version = import_module(parent_module).__version__
                d['@version'] = '{}'.format(module_version)
            except AttributeError:
                d['@version'] = None
        return d
    except AttributeError:
        return json.JSONEncoder.default(self, o)