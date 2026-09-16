def user_name(self, user_id):
    user = self.users.get(user_id)
    if user is None:
        return 'Unknown user ({})'.format(user_id)
    return user['name']