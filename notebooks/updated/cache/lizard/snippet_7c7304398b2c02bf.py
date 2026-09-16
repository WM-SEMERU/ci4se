def req2frame(req, N: int=0):
    if req is None:
        frame = np.arange(N, dtype=np.int64)
    elif isinstance(req, int):
        frame = np.arange(0, N, req, dtype=np.int64)
    elif len(req) == 1:
        frame = np.arange(0, N, req[0], dtype=np.int64)
    elif len(req) == 2:
        frame = np.arange(req[0], req[1], dtype=np.int64)
    elif len(req) == 3:
        frame = np.arange(req[0], req[1], req[2], dtype=np.int64) - 1
    else:
        frame = np.arange(N, dtype=np.int64)
    return frame