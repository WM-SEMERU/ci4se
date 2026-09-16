def get_chunk_size(N, n):
    mem_free = memory()['free']
    if mem_free > 60000000:
        chunks_size = int((mem_free - 10000000) * 1000 / (4 * n * N))
        return chunks_size
    elif mem_free > 40000000:
        chunks_size = int((mem_free - 7000000) * 1000 / (4 * n * N))
        return chunks_size
    elif mem_free > 14000000:
        chunks_size = int((mem_free - 2000000) * 1000 / (4 * n * N))
        return chunks_size
    elif mem_free > 8000000:
        chunks_size = int((mem_free - 1400000) * 1000 / (4 * n * N))
        return chunks_size
    elif mem_free > 2000000:
        chunks_size = int((mem_free - 900000) * 1000 / (4 * n * N))
        return chunks_size
    elif mem_free > 1000000:
        chunks_size = int((mem_free - 400000) * 1000 / (4 * n * N))
        return chunks_size
    else:
        raise MemoryError(
            """
ERROR: DBSCAN_multiplex @ get_chunk_size:
this machine does not have enough free memory to perform the remaining computations.
"""
            )