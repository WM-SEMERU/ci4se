def is_last_child(self, child_pid):
    last_child = self.last_child
    if last_child is None:
        return False
    return last_child == child_pid