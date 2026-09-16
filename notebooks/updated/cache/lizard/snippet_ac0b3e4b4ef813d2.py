def resize_short(src, size, interp=2):
    h, w, _ = src.shape
    if h > w:
        new_h, new_w = size * h // w, size
    else:
        new_h, new_w = size, size * w // h
    return imresize(src, new_w, new_h, interp=_get_interp_method(interp, (h,
        w, new_h, new_w)))