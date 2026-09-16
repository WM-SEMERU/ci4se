def lines_touch_2D(ab, cd):
    return lines_colinear(ab, cd) | np.isfinite(line_intersection_2D(ab, cd)[0]
        )