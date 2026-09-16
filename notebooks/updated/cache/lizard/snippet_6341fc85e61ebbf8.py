def retrieve_manual_indices(self):
    if self.parent_changed:
        pass
    else:
        pbool = map_indices_child2root(child=self.rtdc_ds, child_indices=np
            .where(~self.manual)[0]).tolist()
        pold = self._man_root_ids
        pall = sorted(list(set(pbool + pold)))
        pvis_c = map_indices_root2child(child=self.rtdc_ds, root_indices=pall
            ).tolist()
        pvis_p = map_indices_child2root(child=self.rtdc_ds, child_indices=
            pvis_c).tolist()
        phid = list(set(pall) - set(pvis_p))
        all_idx = list(set(pbool + phid))
        self._man_root_ids = sorted(all_idx)
    return self._man_root_ids