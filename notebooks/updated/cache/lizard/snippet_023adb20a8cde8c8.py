def get_random_user(self):
    from provider.models import User
    u = User.objects.order_by('?')[0]
    return {'username': u.username, 'password': u.password, 'fullname': u.
        fullname}