def get_user_events(self, id, **data):
    return self.get('/users/{0}/events/'.format(id), data=data)