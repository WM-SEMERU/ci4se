def get_user(self, userPk):
    r = self._request('user/' + str(userPk))
    if r:
        u = User()
        u.pk = u.id = userPk
        u.__dict__.update(r.json())
        return u
    return None