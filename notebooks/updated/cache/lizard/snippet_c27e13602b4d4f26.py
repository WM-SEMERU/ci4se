def user(self, username=None, pk=None, **kwargs):
    _users = self.users(username=username, pk=pk, **kwargs)
    if len(_users) == 0:
        raise NotFoundError('No user criteria matches')
    if len(_users) != 1:
        raise MultipleFoundError('Multiple users fit criteria')
    return _users[0]