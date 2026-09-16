def post_event_discounts(self, id, **data):
    return self.post('/events/{0}/discounts/'.format(id), data=data)