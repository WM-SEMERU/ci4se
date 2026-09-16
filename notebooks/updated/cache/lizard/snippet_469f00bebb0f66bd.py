def authors(self, *usernames):
    if len(usernames) == 1:
        return self.filter(**{'author__{}'.format(User.USERNAME_FIELD):
            usernames[0]})
    else:
        return self.filter(**{'author__{}__in'.format(User.USERNAME_FIELD):
            usernames})