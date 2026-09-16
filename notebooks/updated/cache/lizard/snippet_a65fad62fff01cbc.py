def get_git_tag(hash_, git_path='git'):
    tag, status = call((git_path, 'describe', '--exact-match', '--tags',
        hash_), returncode=True)
    if status == 0:
        return tag
    else:
        return None