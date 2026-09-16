def column_order(b1, b2):
    top, left, bottom = 1, 2, 3
    if round(b1[top]) == round(b2[top]) or round(b1[bottom]) == round(b2[
        bottom]):
        return float_cmp(b1[left], b2[left])
    return float_cmp(b1[top], b2[top])