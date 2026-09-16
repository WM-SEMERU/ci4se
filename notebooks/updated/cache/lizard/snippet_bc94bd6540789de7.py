def event(self, name, payload=None, coalesce=True):
    return self.connection.call('event', {'Name': name, 'Payload': payload,
        'Coalesce': coalesce}, expect_body=False)