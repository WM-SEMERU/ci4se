def _edge_group_substitution(self, ndid, nsplit, idxs, sr_tab, ndoffset,
    ed_remove, into_or_from):
    eidxs = idxs[nm.where(self.edges[idxs, 1 - into_or_from] == ndid)[0]]
    for igrp in self.edges_by_group(eidxs):
        if igrp.shape[0] > 1:
            directions = self.edge_dir[igrp[0]]
            edge_indexes = sr_tab[(directions), :].T.flatten() + ndoffset
            self.edges[igrp, 1] = edge_indexes
            if self._edge_weight_table is not None:
                self.edges_weights[igrp] = self._edge_weight_table[1,
                    directions]
        else:
            ed_remove.append(igrp[0])
            nnewed = np.power(nsplit, self.data.ndim - 1)
            muleidxs = nm.tile(igrp, nnewed)
            newed = self.edges[(muleidxs), :]
            neweddir = self.edge_dir[muleidxs]
            local_node_ids = sr_tab[(self.edge_dir[igrp] + self.data.ndim *
                into_or_from), :].T.flatten()
            newed[:, (1 - into_or_from)] = local_node_ids + ndoffset
            if self._edge_weight_table is not None:
                self.add_edges(newed, neweddir, self.edge_group[igrp],
                    edge_low_or_high=1)
            else:
                self.add_edges(newed, neweddir, self.edge_group[igrp],
                    edge_low_or_high=None)
    return ed_remove