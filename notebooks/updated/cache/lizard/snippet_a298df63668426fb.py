def get_user_owned_event_orders(self, id, **data):
    return self.get('/users/{0}/owned_event_orders/'.format(id), data=data)