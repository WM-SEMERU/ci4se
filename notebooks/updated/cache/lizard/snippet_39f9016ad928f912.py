def send(self, event, message):
    self.connection.send({'reason': ['request', 'send'], 'content': {
        'reason': event, 'request_id': self.request_counter, 'content':
        message}})
    self.request_counter = self.request_counter + 1