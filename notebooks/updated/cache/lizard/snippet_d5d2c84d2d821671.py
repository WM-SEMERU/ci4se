def channel_angle(im, chanapproxangle=None, *, isshiftdftedge=False,
    truesize=None):
    im = np.asarray(im)
    if not isshiftdftedge:
        im = edge(im)
    return reg.orientation_angle(im, isshiftdft=isshiftdftedge, approxangle
        =chanapproxangle, truesize=truesize)