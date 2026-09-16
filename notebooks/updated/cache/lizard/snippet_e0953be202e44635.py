def uid_exists(uid):
    try:
        pwd.getpwuid(uid)
        uid_exists = True
    except KeyError:
        uid_exists = False
    return uid_exists