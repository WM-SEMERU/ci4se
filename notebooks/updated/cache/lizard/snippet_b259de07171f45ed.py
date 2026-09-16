def end_connect(self, shape, cxn_pt_idx):
    self._connect_end_to(shape, cxn_pt_idx)
    self._move_end_to_cxn(shape, cxn_pt_idx)