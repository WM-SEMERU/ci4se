def matches(self, client, event_data):
    for f in self.filters:
        if not f(client, event_data):
            return False
    return True