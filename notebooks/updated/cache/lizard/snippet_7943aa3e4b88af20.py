def shot_create_asset(self, *args, **kwargs):
    if not self.cur_shot:
        return
    asset = self.create_asset(project=self.cur_shot.project, shot=self.cur_shot
        )
    if not asset:
        return
    atypes = {}
    for c in self.shot_asset_model.root.childItems:
        atypes[c.internal_data()] = c
    atypeitem = atypes.get(asset.atype)
    if not atypeitem:
        atypedata = djitemdata.AtypeItemData(asset.atype)
        atypeitem = treemodel.TreeItem(atypedata, self.shot_asset_model.root)
        atypes[asset.atype] = atypeitem
    assetdata = djitemdata.AssetItemData(asset)
    treemodel.TreeItem(assetdata, atypeitem)