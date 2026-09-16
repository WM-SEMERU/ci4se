def enable(cls, user_id, github_id, name, hook):
    try:
        repo = cls.get(user_id, github_id=github_id, name=name)
    except NoResultFound:
        repo = cls.create(user_id=user_id, github_id=github_id, name=name)
    repo.hook = hook
    repo.user_id = user_id
    return repo