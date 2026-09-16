def xy_reading_order(e1, e2):
    b1 = e1.bbox
    b2 = e2.bbox
    if round(b1[x0]) == round(b2[x0]):
        return float_cmp(b1[y0], b2[y0])
    return float_cmp(b1[x0], b2[x0])