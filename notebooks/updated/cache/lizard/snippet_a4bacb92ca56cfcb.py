def _run_as(user, group):

    def wrapper():
        if user is not None:
            os.setuid(user)
        if group is not None:
            os.setgid(group)
    return wrapper