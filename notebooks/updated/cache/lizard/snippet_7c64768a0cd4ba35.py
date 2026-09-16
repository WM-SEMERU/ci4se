def invite(self, event):
    self.log('Inviting new user to enrol')
    name = event.data['name']
    email = event.data['email']
    method = event.data['method']
    self._invite(name, method, email, event.client.uuid, event)