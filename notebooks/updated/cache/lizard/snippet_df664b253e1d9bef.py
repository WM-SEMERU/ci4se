def overlap_add(blk_sig, size=None, hop=None, wnd=None, normalize=True):
    import numpy as np
    if size is None:
        blk_sig = Stream(blk_sig)
        size = len(blk_sig.peek())
    if hop is None:
        hop = size
    if wnd is None:
        wnd = np.ones(size)
    elif callable(wnd) and not isinstance(wnd, Stream):
        wnd = wnd(size)
    if isinstance(wnd, Sequence):
        wnd = np.array(wnd)
    elif isinstance(wnd, Iterable):
        wnd = np.hstack(wnd)
    else:
        raise TypeError('Window should be an iterable or a callable')
    if normalize:
        steps = Stream(wnd).blocks(hop).map(np.array)
        gain = np.sum(np.abs(np.vstack(steps)), 0).max()
        if gain:
            wnd = wnd / gain
    old = np.zeros(size)
    for blk in (wnd * blk for blk in blk_sig):
        blk[:-hop] += old[hop:]
        for el in blk[:hop]:
            yield el
        old = blk
    for el in old[hop:]:
        yield el