def show_user(self, user):
    res = self.post('loadUsers', {'userId': user})
    if isinstance(res, list) and len(res) > 0:
        res = res[0]
    return _fix_user(res)