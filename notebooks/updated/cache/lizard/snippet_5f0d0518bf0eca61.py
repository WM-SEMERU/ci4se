def edge_just(left, right, width, fillchar=' ', min_padding_length=1):
    assert unicode_width(fillchar) == 1, 'fillchar must be single-width char'
    padding = fillchar * max(min_padding_length, width - unicode_width(left +
        right))
    return left + padding + right