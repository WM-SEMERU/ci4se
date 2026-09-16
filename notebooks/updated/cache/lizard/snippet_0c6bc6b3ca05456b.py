def _notify(self, task, message):
    if self.notify_func:
        message = common.to_utf8(message.strip())
        title = common.to_utf8('Focus ({0})'.format(task.name))
        self.notify_func(title, message)