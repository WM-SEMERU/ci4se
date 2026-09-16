def group_tasks(self):
    tasks = set()
    for node in walk_tree(self):
        for ctrl in node.controllers.values():
            tasks.update(ctrl.tasks)
    return tasks