def fetchSynIdxCell(self, cell, nidx, synParams):
    syn_idx = []
    for i, zz in enumerate(self.layerBoundaries):
        if nidx[i] == 0:
            syn_idx.append(np.array([], dtype=int))
        else:
            syn_idx.append(cell.get_rand_idx_area_norm(section=synParams[
                'section'], nidx=nidx[i], z_min=zz.min(), z_max=zz.max()).
                astype('int16'))
    return syn_idx