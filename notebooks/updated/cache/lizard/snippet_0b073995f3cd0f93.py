def merge_metas(*metas):
    metadict = {}
    for meta in metas:
        metadict.update(meta.__dict__)
    metadict = {k: v for k, v in metadict.items() if not k.startswith('__')}
    return type('Meta', (object,), metadict)