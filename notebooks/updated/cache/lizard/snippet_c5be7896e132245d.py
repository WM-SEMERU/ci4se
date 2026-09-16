def is_horz_aligned(c):
    return all([(_to_span(c[i]).sentence.is_visual() and bbox_horz_aligned(
        bbox_from_span(_to_span(c[i])), bbox_from_span(_to_span(c[0])))) for
        i in range(len(c))])