def make_reply(self):
    return Message(to=str(self.sender), sender=str(self.to), body=self.body,
        thread=self.thread, metadata=self.metadata)