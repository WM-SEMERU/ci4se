def commit_hash(self):
    commit_hash = None
    branch = None
    branch_file = '.git/HEAD'
    if os.path.isfile(branch_file):
        with open(branch_file, 'r') as f:
            try:
                branch = f.read().strip().split('/')[2]
            except IndexError:
                pass
        if branch:
            hash_file = '.git/refs/heads/{}'.format(branch)
            if os.path.isfile(hash_file):
                with open(hash_file, 'r') as f:
                    commit_hash = f.read().strip()
    return commit_hash