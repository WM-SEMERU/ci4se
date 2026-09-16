def remove(self, idxs):
    import utool as ut
    keep_idxs = ut.index_complement(idxs, len(self))
    return self.take(keep_idxs)