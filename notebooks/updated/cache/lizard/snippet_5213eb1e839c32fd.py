def round_to_chunk_size(self, chunk_size, offset=Vec(0, 0, 0, dtype=int)):
    chunk_size = np.array(chunk_size, dtype=np.float32)
    result = self.clone()
    result = result - offset
    result.minpt = np.round(result.minpt / chunk_size) * chunk_size
    result.maxpt = np.round(result.maxpt / chunk_size) * chunk_size
    return (result + offset).astype(self.dtype)