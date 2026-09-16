def create_default_links(self):
    self._plm.manage_aldb_record(64, 226, 0, self.address, self.cat, self.
        subcat, self.product_key)
    self.manage_aldb_record(65, 162, 0, self._plm.address, self._plm.cat,
        self._plm.subcat, self._plm.product_key)
    for link in self._stateList:
        state = self._stateList[link]
        if state.is_responder:
            self._plm.manage_aldb_record(64, 226, link, self._address, 0, 0, 0)
            self.manage_aldb_record(65, 162, link, self._plm.address, state
                .linkdata1, state.linkdata2, state.linkdata3)
        if state.is_controller:
            self._plm.manage_aldb_record(65, 162, link, self._address, 0, 0, 0)
            self.manage_aldb_record(64, 226, link, self._plm.address, 0, 0, 0)
    self.read_aldb()