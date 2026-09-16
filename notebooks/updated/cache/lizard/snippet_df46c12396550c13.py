def view_shot(self, shot):
    log.debug('Viewing shot %s', shot.name)
    self.cur_shot = None
    self.pages_tabw.setCurrentIndex(3)
    self.shot_name_le.setText(shot.name)
    self.shot_prj_le.setText(shot.project.name)
    self.shot_seq_le.setText(shot.sequence.name)
    self.shot_start_sb.setValue(shot.startframe)
    self.shot_end_sb.setValue(shot.endframe)
    self.shot_handle_sb.setValue(shot.handlesize)
    self.shot_desc_pte.setPlainText(shot.description)
    assetsrootdata = treemodel.ListItemData(['Name', 'Description'])
    assetsrootitem = treemodel.TreeItem(assetsrootdata)
    self.shot_asset_model = treemodel.TreeModel(assetsrootitem)
    self.shot_asset_treev.setModel(self.shot_asset_model)
    atypes = {}
    assets = shot.assets.all()
    for a in assets:
        atype = a.atype
        atypeitem = atypes.get(atype)
        if not atypeitem:
            atypedata = djitemdata.AtypeItemData(atype)
            atypeitem = treemodel.TreeItem(atypedata, assetsrootitem)
            atypes[atype] = atypeitem
        assetdata = djitemdata.AssetItemData(a)
        treemodel.TreeItem(assetdata, atypeitem)
    tasksrootdata = treemodel.ListItemData(['Name', 'Short'])
    tasksrootitem = treemodel.TreeItem(tasksrootdata)
    self.shot_task_model = treemodel.TreeModel(tasksrootitem)
    self.shot_task_tablev.setModel(self.shot_task_model)
    tasks = shot.tasks.all()
    for t in tasks:
        tdata = djitemdata.TaskItemData(t)
        treemodel.TreeItem(tdata, tasksrootitem)
    self.cur_shot = shot