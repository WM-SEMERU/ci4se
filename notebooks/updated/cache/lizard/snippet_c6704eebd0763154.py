def contained_segments_matrix(segments):
    x1, y1 = segments[:, (0)], segments[:, (1)]
    x2, y2 = x1 + segments[:, (2)], y1 + segments[:, (3)]
    n = len(segments)
    x1so, x2so, y1so, y2so = list(map(numpy.argsort, (x1, x2, y1, y2)))
    x1soi, x2soi, y1soi, y2soi = list(map(numpy.argsort, (x1so, x2so, y1so,
        y2so)))
    o1 = numpy.triu(numpy.ones((n, n)), k=1).astype(bool)
    o2 = numpy.tril(numpy.ones((n, n)), k=0).astype(bool)
    a_inside_b_x = o2[x1soi][:, (x1soi)] * o1[x2soi][:, (x2soi)]
    a_inside_b_y = o2[y1soi][:, (y1soi)] * o1[y2soi][:, (y2soi)]
    a_inside_b = a_inside_b_x * a_inside_b_y
    return a_inside_b