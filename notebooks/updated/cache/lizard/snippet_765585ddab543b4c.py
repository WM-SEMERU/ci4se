def fix_abicritical(self):
    count = 0
    for task in self.iflat_tasks(status=self.S_ABICRITICAL):
        count += task.fix_abicritical()
    return count