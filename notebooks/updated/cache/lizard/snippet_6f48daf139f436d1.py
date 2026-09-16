def delete_user(self, auth, username):
    path = '/admin/users/{}'.format(username)
    self.delete(path, auth=auth)