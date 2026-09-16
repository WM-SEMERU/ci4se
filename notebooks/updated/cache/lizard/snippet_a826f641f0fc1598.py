def from_linearized(first, second, intersections):
    s, t, success = segment_intersection(first.start_node, first.end_node,
        second.start_node, second.end_node)
    bad_parameters = False
    if success:
        if not (_helpers.in_interval(s, 0.0, 1.0) and _helpers.in_interval(
            t, 0.0, 1.0)):
            bad_parameters = True
    else:
        if first.error == 0.0 and second.error == 0.0:
            raise ValueError(_UNHANDLED_LINES)
        bad_parameters = True
        s = 0.5
        t = 0.5
    if bad_parameters:
        if not convex_hull_collide(first.curve.nodes, second.curve.nodes):
            return
    orig_s = (1 - s) * first.curve.start + s * first.curve.end
    orig_t = (1 - t) * second.curve.start + t * second.curve.end
    refined_s, refined_t = _intersection_helpers.full_newton(orig_s, first.
        curve.original_nodes, orig_t, second.curve.original_nodes)
    refined_s, success = _helpers.wiggle_interval(refined_s)
    if not success:
        return
    refined_t, success = _helpers.wiggle_interval(refined_t)
    if not success:
        return
    add_intersection(refined_s, refined_t, intersections)