def get_rendition_fit_size(spec, input_w, input_h, output_scale):
    width = input_w
    height = input_h
    scale = spec.get('scale')
    if scale:
        width = width / scale
        height = height / scale
    min_width = spec.get('scale_min_width')
    if min_width and width < min_width:
        height = height * min_width / width
        width = min_width
    min_height = spec.get('scale_min_height')
    if min_height and height < min_height:
        width = width * min_height / height
        height = min_height
    tgt_width, tgt_height = spec.get('width'), spec.get('height')
    if tgt_width and width > tgt_width:
        height = height * tgt_width / width
        width = tgt_width
    if tgt_height and height > tgt_height:
        width = width * tgt_height / height
        height = tgt_height
    tgt_width, tgt_height = spec.get('max_width'), spec.get('max_height')
    if tgt_width and width > tgt_width:
        height = height * tgt_width / width
        width = tgt_width
    if tgt_height and height > tgt_height:
        width = width * tgt_height / height
        height = tgt_height
    width = width * output_scale
    height = height * output_scale
    width = min(round(width), input_w)
    height = min(round(height), input_h)
    return (width, height), None