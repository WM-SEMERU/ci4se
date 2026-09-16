def compose(layers, bbox=None, layer_filter=None, color=None, **kwargs):
    from PIL import Image
    if not hasattr(layers, '__iter__'):
        layers = [layers]

    def _default_filter(layer):
        return layer.is_visible()
    layer_filter = layer_filter or _default_filter
    valid_layers = [x for x in layers if layer_filter(x)]
    if len(valid_layers) == 0:
        return None
    if bbox is None:
        bbox = extract_bbox(valid_layers)
        if bbox == (0, 0, 0, 0):
            return None
    mode = get_pil_mode(valid_layers[0]._psd.color_mode, True)
    result = Image.new(mode, (bbox[2] - bbox[0], bbox[3] - bbox[1]), color=
        color if color is not None else 'white')
    result.putalpha(0)
    for layer in valid_layers:
        if intersect(layer.bbox, bbox) == (0, 0, 0, 0):
            continue
        image = layer.compose(**kwargs)
        if image is None:
            continue
        logger.debug('Composing %s' % layer)
        offset = layer.left - bbox[0], layer.top - bbox[1]
        result = _blend(result, image, offset)
    return result