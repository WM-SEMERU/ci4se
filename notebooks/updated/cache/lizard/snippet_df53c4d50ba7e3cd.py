def from_multi_segment_list(cls, description, segmentlists, names, ifos,
    seg_summ_lists=None, **kwargs):
    seglistdict = segments.segmentlistdict()
    for name, ifo, segmentlist in zip(names, ifos, segmentlists):
        seglistdict[ifo + ':' + name] = segmentlist
    if seg_summ_lists is not None:
        seg_summ_dict = segments.segmentlistdict()
        for name, ifo, seg_summ_list in zip(names, ifos, seg_summ_lists):
            seg_summ_dict[ifo + ':' + name] = seg_summ_list
    else:
        seg_summ_dict = None
    return cls.from_segment_list_dict(description, seglistdict,
        seg_summ_dict=seg_summ_dict, **kwargs)