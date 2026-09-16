def validate_intervals(ref_intervals, est_intervals):
    if ref_intervals.size == 0:
        warnings.warn('Reference notes are empty.')
    if est_intervals.size == 0:
        warnings.warn('Estimated notes are empty.')
    util.validate_intervals(ref_intervals)
    util.validate_intervals(est_intervals)