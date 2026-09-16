def query_cumulative_flags(ifo, segment_names, start_time, end_time, source
    ='any', server='segments.ligo.org', veto_definer=None, bounds=None,
    padding=None, override_ifos=None, cache=False):
    total_segs = segmentlist([])
    for flag_name in segment_names:
        ifo_name = ifo
        if override_ifos is not None and flag_name in override_ifos:
            ifo_name = override_ifos[flag_name]
        segs = query_flag(ifo_name, flag_name, start_time, end_time, source
            =source, server=server, veto_definer=veto_definer, cache=cache)
        if padding and flag_name in padding:
            s, e = padding[flag_name]
            segs2 = segmentlist([])
            for seg in segs:
                segs2.append(segment(seg[0] + s, seg[1] + e))
            segs = segs2
        if bounds is not None and flag_name in bounds:
            s, e = bounds[flag_name]
            valid = segmentlist([segment([s, e])])
            segs = (segs & valid).coalesce()
        total_segs = (total_segs + segs).coalesce()
    return total_segs