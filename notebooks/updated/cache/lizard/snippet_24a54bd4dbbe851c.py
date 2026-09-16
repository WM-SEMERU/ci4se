def authenticate(self, username='', password='', **kwargs):
    try:
        user = get_user_model().objects.filter(email__iexact=username)[0]
        if check_password(password, user.password):
            return user
        else:
            return None
    except IndexError:
        return None