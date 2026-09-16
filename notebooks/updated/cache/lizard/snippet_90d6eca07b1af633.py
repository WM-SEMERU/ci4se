def task_remove_user(self, *args, **kwargs):
    if not self.cur_task:
        return
    i = self.task_user_tablev.currentIndex()
    item = i.internalPointer()
    if item:
        user = item.internal_data()
        self.cur_task.users.remove(user)
        item.set_parent(None)