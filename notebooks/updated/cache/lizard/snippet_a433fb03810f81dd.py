def remove(self, slide_layout):
    if slide_layout.used_by_slides:
        raise ValueError(
            'cannot remove slide-layout in use by one or more slides')
    target_idx = self.index(slide_layout)
    target_sldLayoutId = self._sldLayoutIdLst.sldLayoutId_lst[target_idx]
    self._sldLayoutIdLst.remove(target_sldLayoutId)
    slide_layout.slide_master.part.drop_rel(target_sldLayoutId.rId)