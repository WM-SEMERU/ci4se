def user_lists(self, username, member_type='USER'):
    return self.client.service.getUserLists(username, member_type, self.
        proxy_id)