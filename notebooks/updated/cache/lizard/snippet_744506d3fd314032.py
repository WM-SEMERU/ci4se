def write(tsdict, outfile, start=None, end=None, name='gwpy', run=0):
    if not start:
        start = list(tsdict.values())[0].xspan[0]
    if not end:
        end = list(tsdict.values())[0].xspan[1]
    duration = end - start
    detectors = 0
    for series in tsdict.values():
        try:
            idx = list(lalutils.LAL_DETECTORS.keys()).index(series.channel.ifo)
            detectors |= 1 << 2 * idx
        except (KeyError, AttributeError):
            continue
    frame = lalframe.FrameNew(start, duration, name, run, 0, detectors)
    for series in tsdict.values():
        lalseries = series.to_lal()
        add_ = lalutils.find_typed_function(series.dtype, 'FrameAdd',
            'TimeSeriesProcData', module=lalframe)
        add_(frame, lalseries)
    lalframe.FrameWrite(frame, outfile)