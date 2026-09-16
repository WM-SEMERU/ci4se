def mapLayers(name=None, types=None):
    if types is not None and not isinstance(types, list):
        types = [types]
    layers = _layerreg.mapLayers().values()
    _layers = []
    if name or types:
        if name:
            _layers = [layer for layer in layers if re.match(name, layer.
                name())]
        if types:
            _layers += [layer for layer in layers if layer.type() in types]
        return _layers
    else:
        return layers