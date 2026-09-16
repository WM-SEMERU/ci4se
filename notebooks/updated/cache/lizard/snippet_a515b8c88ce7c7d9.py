def split_box(fraction, x, y, w, h):
    if w >= h:
        new_w = int(w * fraction)
        if new_w:
            return (x, y, new_w, h), (x + new_w, y, w - new_w, h)
        else:
            return None, None
    else:
        new_h = int(h * fraction)
        if new_h:
            return (x, y, w, new_h), (x, y + new_h, w, h - new_h)
        else:
            return None, None