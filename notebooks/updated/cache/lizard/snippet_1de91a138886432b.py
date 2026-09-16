def associate_psds_to_multi_ifo_segments(opt, fd_segments, gwstrain, flen,
    delta_f, flow, ifos, dyn_range_factor=1.0, precision=None):
    for ifo in ifos:
        if gwstrain is not None:
            strain = gwstrain[ifo]
        else:
            strain = None
        if fd_segments is not None:
            segments = fd_segments[ifo]
        else:
            segments = None
        associate_psds_to_single_ifo_segments(opt, segments, strain, flen,
            delta_f, flow, ifo, dyn_range_factor=dyn_range_factor,
            precision=precision)