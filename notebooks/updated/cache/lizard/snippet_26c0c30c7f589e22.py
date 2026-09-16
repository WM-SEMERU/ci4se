def tag_new_version(version: str):
    check_repo()
    return repo.git.tag('-a', 'v{0}'.format(version), m='v{0}'.format(version))