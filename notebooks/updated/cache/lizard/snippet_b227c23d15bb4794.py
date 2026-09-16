def ncores_reserved(self):
    return sum(task.manager.num_cores for task in self if task.status ==
        task.S_SUB)