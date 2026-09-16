def calcuate_bboxes(im_shape, patch_size):
    h, w = im_shape
    ph, pw = patch_size
    steps_h = chain(range(0, h - ph, ph), [h - ph])
    steps_w = chain(range(0, w - pw, pw), [w - pw])
    return product(steps_h, steps_w)