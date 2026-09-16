def knot_insertion_kv(knotvector, u, span, r):
    kv_size = len(knotvector)
    kv_updated = [(0.0) for _ in range(kv_size + r)]
    for i in range(0, span + 1):
        kv_updated[i] = knotvector[i]
    for i in range(1, r + 1):
        kv_updated[span + i] = u
    for i in range(span + 1, kv_size):
        kv_updated[i + r] = knotvector[i]
    return kv_updated