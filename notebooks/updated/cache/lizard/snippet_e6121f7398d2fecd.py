def full_tasktrace(self):
    if self.prev_error:
        return self.prev_error.tasktrace + self.tasktrace
    else:
        return self.tasktrace