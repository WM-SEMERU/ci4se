def create_user(username, password, **kwargs):
    try:
        User = get_model('user')
        user = User.get(User.c.username == username)
        if user:
            return False, {'username': 'Username is already existed!'}
        user = User(username=username, password=password, **kwargs)
        user.set_password(password)
        user.save()
        return True, user
    except Exception as e:
        log.exception(e)
        return False, {'_': 'Creating user failed!'}