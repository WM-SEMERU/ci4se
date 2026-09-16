def create_asset_model(self, project, releasetype):
    rootdata = treemodel.ListItemData(['Name'])
    rootitem = treemodel.TreeItem(rootdata)
    for atype in project.atype_set.all():
        atypedata = djitemdata.AtypeItemData(atype)
        atypeitem = treemodel.TreeItem(atypedata, rootitem)
        for asset in atype.asset_set.filter(project=project):
            assetdata = djitemdata.AssetItemData(asset)
            assetitem = treemodel.TreeItem(assetdata, atypeitem)
            for task in asset.tasks.all():
                taskdata = djitemdata.TaskItemData(task)
                taskitem = treemodel.TreeItem(taskdata, assetitem)
                taskfiles = task.taskfile_set.filter(releasetype=
                    releasetype, typ=self._filetype)
                for d in taskfiles.order_by('descriptor').values_list(
                    'descriptor', flat=True).distinct():
                    ddata = treemodel.ListItemData([d])
                    treemodel.TreeItem(ddata, taskitem)
    assetmodel = treemodel.TreeModel(rootitem)
    return assetmodel