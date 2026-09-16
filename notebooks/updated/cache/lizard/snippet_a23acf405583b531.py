def _rebuild_blknos_and_blklocs(self):
    new_blknos = np.empty(self.shape[0], dtype=np.int64)
    new_blklocs = np.empty(self.shape[0], dtype=np.int64)
    new_blknos.fill(-1)
    new_blklocs.fill(-1)
    for blkno, blk in enumerate(self.blocks):
        rl = blk.mgr_locs
        new_blknos[rl.indexer] = blkno
        new_blklocs[rl.indexer] = np.arange(len(rl))
    if (new_blknos == -1).any():
        raise AssertionError('Gaps in blk ref_locs')
    self._blknos = new_blknos
    self._blklocs = new_blklocs