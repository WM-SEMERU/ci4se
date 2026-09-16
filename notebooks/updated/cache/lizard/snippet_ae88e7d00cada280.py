def validate_hier_intervals(intervals_hier):
    label_top = util.generate_labels(intervals_hier[0])
    boundaries = set(util.intervals_to_boundaries(intervals_hier[0]))
    for level, intervals in enumerate(intervals_hier[1:], 1):
        label_current = util.generate_labels(intervals)
        validate_structure(intervals_hier[0], label_top, intervals,
            label_current)
        new_bounds = set(util.intervals_to_boundaries(intervals))
        if boundaries - new_bounds:
            warnings.warn('Segment hierarchy is inconsistent at level {:d}'
                .format(level))
        boundaries |= new_bounds