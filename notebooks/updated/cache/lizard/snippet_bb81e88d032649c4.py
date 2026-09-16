def _find_to_filter(in_file, exclude_file, params, to_exclude):
    for feat in pybedtools.BedTool(in_file).intersect(pybedtools.BedTool(
        exclude_file), wao=True, nonamecheck=True):
        (us_chrom, us_start, us_end, name, other_chrom, other_start,
            other_end, overlap) = feat.fields
        if float(overlap) > 0:
            other_size = float(other_end) - float(other_start)
            other_pct = float(overlap) / other_size
            us_pct = float(overlap) / (float(us_end) - float(us_start))
            if us_pct > params['sv_pct'] or other_pct > params['rpt_pct']:
                to_exclude[name].append(float(overlap))
    return to_exclude