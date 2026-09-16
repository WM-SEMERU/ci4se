def update_local_rt_nlris(self):
    current_conf_import_rts = set()
    for vrf in self._vrfs_conf.vrf_confs:
        current_conf_import_rts.update(vrf.import_rts)
    removed_rts = self._all_vrfs_import_rts_set - current_conf_import_rts
    new_rts = current_conf_import_rts - self._all_vrfs_import_rts_set
    self._all_vrfs_import_rts_set = current_conf_import_rts
    for new_rt in new_rts:
        self.add_rt_nlri(new_rt)
    for removed_rt in removed_rts:
        self.add_rt_nlri(removed_rt, is_withdraw=True)