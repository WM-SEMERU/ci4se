def i2s_frameid(x):
    try:
        return PNIO_FRAME_IDS[x]
    except KeyError:
        pass
    if 256 <= x < 4096:
        return 'RT_CLASS_3 (%4x)' % x
    if 32768 <= x < 49152:
        return 'RT_CLASS_1 (%4x)' % x
    if 49152 <= x < 64512:
        return 'RT_CLASS_UDP (%4x)' % x
    if 65408 <= x < 65424:
        return 'FragmentationFrameID (%4x)' % x
    return x