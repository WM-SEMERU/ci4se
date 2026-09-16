def asset_taskfile_sel_changed(self, tf):
    self.asset_open_pb.setEnabled(bool(tf))
    enablenew = bool(self.browser.assetbrws.selected_indexes(1)
        ) and self.browser.get_releasetype() == djadapter.RELEASETYPES['work']
    self.asset_save_pb.setEnabled(enablenew)
    self.asset_descriptor_le.setEnabled(enablenew)
    self.asset_comment_pte.setEnabled(enablenew)
    self.update_descriptor_le(self.asset_descriptor_le, tf)