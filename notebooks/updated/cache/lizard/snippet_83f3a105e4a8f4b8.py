def create_asset_model(self):
    rootdata = treemodel.ListItemData(['Name'])
    rootitem = treemodel.TreeItem(rootdata)
    prjs = djadapter.projects.all()
    for prj in prjs:
        prjdata = djitemdata.ProjectItemData(prj)
        prjitem = treemodel.TreeItem(prjdata, rootitem)
        for atype in prj.atype_set.all():
            atypedata = djitemdata.AtypeItemData(atype)
            atypeitem = treemodel.TreeItem(atypedata, prjitem)
            for asset in atype.asset_set.filter(project=prj):
                assetdata = djitemdata.AssetItemData(asset)
                assetitem = treemodel.TreeItem(assetdata, atypeitem)
                for typ in self.refobjinter.get_available_types_for_scene(asset
                    ):
                    typdata = treemodel.ListItemData([typ])
                    treemodel.TreeItem(typdata, assetitem)
    return treemodel.TreeModel(rootitem)