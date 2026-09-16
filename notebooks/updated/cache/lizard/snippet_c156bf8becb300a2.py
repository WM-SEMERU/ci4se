def normalizeDefaultLayerName(value, font):
    value = normalizeLayerName(value)
    if value not in font.layerOrder:
        raise ValueError("No layer with the name '%s' exists." % value)
    return unicode(value)