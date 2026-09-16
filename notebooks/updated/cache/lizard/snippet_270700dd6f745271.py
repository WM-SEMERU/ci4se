def get_user_contact_list(self, id, contact_list_id, **data):
    return self.get('/users/{0}/contact_lists/{0}/'.format(id,
        contact_list_id), data=data)