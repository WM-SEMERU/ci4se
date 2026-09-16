def shot_create_task(self, *args, **kwargs):
    if not self.cur_shot:
        return
    task = self.create_task(element=self.cur_shot)
    if task:
        taskdata = djitemdata.TaskItemData(task)
        treemodel.TreeItem(taskdata, self.shot_task_model.root)