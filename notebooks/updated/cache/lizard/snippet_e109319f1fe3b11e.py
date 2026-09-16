def get_uid(user=None):
    if not HAS_PWD:
        return None
    elif user is None:
        try:
            return os.geteuid()
        except AttributeError:
            return None
    else:
        try:
            return pwd.getpwnam(user).pw_uid
        except KeyError:
            return None