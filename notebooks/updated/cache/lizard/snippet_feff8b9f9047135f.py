def get_by_username(cls, username):
    return cls.query.filter(UserProfile._username == username.lower()).one()