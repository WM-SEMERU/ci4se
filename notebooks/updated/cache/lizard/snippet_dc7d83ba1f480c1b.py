def get_children(self):
    if self.is_file:
        return self.filechildren
    children = []
    for work in self.flow:
        if work.depends_on(self):
            children.append(work)
        for task in work:
            if task.depends_on(self):
                children.append(task)
    return children