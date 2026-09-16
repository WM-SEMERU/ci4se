def _compute_focal_depth_term(self, C, rup):
    if rup.hypo_depth > 120.0:
        z_h = 120.0
    else:
        z_h = rup.hypo_depth
    return C['theta11'] * (z_h - 60.0)