def check_inasafe_fields(layer, keywords_only=False):
    inasafe_fields = layer.keywords['inasafe_fields']
    real_fields = [field.name() for field in layer.fields().toList()]
    inasafe_fields_flat = []
    for value in list(inasafe_fields.values()):
        if isinstance(value, list):
            inasafe_fields_flat.extend(value)
        else:
            inasafe_fields_flat.append(value)
    difference = set(inasafe_fields_flat).difference(real_fields)
    if len(difference):
        message = tr(
            'inasafe_fields has more fields than the layer %s itself : %s' %
            (layer.keywords['layer_purpose'], difference))
        raise InvalidLayerError(message)
    if keywords_only:
        return True
    difference = set(real_fields).difference(inasafe_fields_flat)
    if len(difference):
        message = tr(
            'The layer %s has more fields than inasafe_fields : %s' % (
            layer.title(), difference))
        raise InvalidLayerError(message)
    return True