def get_series_events(self, id, **data):
    return self.get('/series/{0}/events/'.format(id), data=data)