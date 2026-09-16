def split_evenly(n, chunks):
    if n < chunks:
        raise ChunkingError('Number of chunks is greater than number')
    if n % chunks == 0:
        return [n / chunks] * chunks
    max_size = n / chunks + 1
    return [max_size] + split_evenly(n - max_size, chunks - 1)