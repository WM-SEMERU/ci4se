def message(self, text):
    self.client.publish(self.keys.external, '{}: {}'.format(self.resource,
        text))