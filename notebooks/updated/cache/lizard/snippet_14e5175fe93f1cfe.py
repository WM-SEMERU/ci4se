def grid_time(time, remove_edges=False):
    nt = time.shape[0]
    nx = time.shape[1]
    xnt = np.isfinite(time).sum(axis=0)
    xid = np.argmax(xnt)
    w = np.linalg.lstsq(np.array([np.arange(nt)[~time.mask[:, (xid)]], np.
        ones(nt)[~time.mask[:, (xid)]]]).T, time[:, (xid)][~time.mask[:, (
        xid)]])[0]
    t = w[0] * np.arange(nt) + w[1]
    return t