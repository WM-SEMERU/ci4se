def get_task(self, taskName):
    if taskName[:2] != '- ':
        taskName = '- ' + taskName
    task = None
    try:
        self.refresh
    except:
        pass
    for t in self.tasks:
        if t.title.lower() == taskName.lower() and task == None:
            task = t
            break
    if task == None:
        for t in self.tasks:
            task = t.get_task(taskName)
            if task:
                break
    if task == None and '<Task ' not in self.__repr__():
        for p in self.projects:
            task = p.get_task(taskName)
            if task:
                break
    return task