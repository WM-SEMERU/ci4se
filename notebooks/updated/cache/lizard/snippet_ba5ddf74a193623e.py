def _locate_point(nodes, degree, x_val, y_val):
    r
    candidates = [(1.0, 1.0, 1.0, nodes)]
    for _ in six.moves.xrange(MAX_LOCATE_SUBDIVISIONS + 1):
        next_candidates = []
        for candidate in candidates:
            update_locate_candidates(candidate, next_candidates, x_val,
                y_val, degree)
        candidates = next_candidates
    if not candidates:
        return None
    s_approx, t_approx = mean_centroid(candidates)
    s, t = newton_refine(nodes, degree, x_val, y_val, s_approx, t_approx)
    actual = _surface_helpers.evaluate_barycentric(nodes, degree, 1.0 - s -
        t, s, t)
    expected = np.asfortranarray([x_val, y_val])
    if not _helpers.vector_close(actual.ravel(order='F'), expected, eps=
        LOCATE_EPS):
        s, t = newton_refine(nodes, degree, x_val, y_val, s, t)
    return s, t