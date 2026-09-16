def fetch(self):
    if self.message_id is None:
        raise Exception('.message_id not set.')
    response = self.session.request('find:Message.content', [self.message_id])
    if response == None:
        raise Exception('Message not found.')
    self.data = response
    return self