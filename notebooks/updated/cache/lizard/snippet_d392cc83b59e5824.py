def get_local_user(username):
    try:
        _ = getpwnam(username)
        luser = username
    except KeyError:
        luser = getuser()
    return luser