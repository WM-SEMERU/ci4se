def update_trusted(self, auth_id, auth_secret, event_key):
    self.session.headers.update({'X-TBA-Auth-Id': auth_id})
    self.auth_secret = auth_secret
    self.event_key = event_key