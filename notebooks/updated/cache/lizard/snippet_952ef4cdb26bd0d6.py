def _scatter_list(self, data, owner):
    rank = self.comm.rank
    size = self.comm.size
    subject_submatrices = []
    nblocks = self.comm.bcast(len(data) if rank == owner else None, root=owner)
    for idx in range(0, nblocks, size):
        padded = None
        extra = max(0, idx + size - nblocks)
        if data is not None:
            padded = data[idx:idx + size]
            if extra > 0:
                padded = padded + [None] * extra
        mytrans = self.comm.scatter(padded, root=owner)
        if mytrans is not None:
            subject_submatrices += [mytrans]
    return subject_submatrices