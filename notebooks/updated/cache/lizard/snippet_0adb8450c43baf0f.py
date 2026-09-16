def get_event_access_codes(self, id, **data):
    return self.get('/events/{0}/access_codes/'.format(id), data=data)