def get_user_contact_lists(self, id, **data):
    return self.get('/users/{0}/contact_lists/'.format(id), data=data)