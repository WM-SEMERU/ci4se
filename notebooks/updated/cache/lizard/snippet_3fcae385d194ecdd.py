def interrupt(self, threadId=None):
    back = self.backend()
    if back:
        back.interrupt(threadId)