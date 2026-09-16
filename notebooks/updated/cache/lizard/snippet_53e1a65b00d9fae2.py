def get_order(self, id, **data):
    return self.get('/orders/{0}/'.format(id), data=data)