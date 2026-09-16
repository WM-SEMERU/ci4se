def asset_view_atype(self):
    if not self.cur_asset:
        return
    atype = self.cur_asset.atype
    self.view_atype(atype)