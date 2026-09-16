def add_users(self, users=None):
    if not users:
        raise ArgumentError(
            'You must specify emails for users to add to the user group')
    ulist = {'user': [user for user in users]}
    return self.append(add=ulist)