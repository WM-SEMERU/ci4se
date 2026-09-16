def load_users(path=settings.LOGIN_FILE):
    if not os.path.exists(path):
        return {}
    data = ''
    with open(path) as f:
        data = f.read().splitlines()
    users = {}
    cnt = 1
    for line in data:
        line = line.split(':')
        assert len(line) == 7, "Bad number of fields in '%s', at line %d!" % (
            path, cnt)
        users[line[0]] = {'pass_hash': line[1], 'uid': line[2], 'gid': line
            [3], 'full_name': line[4], 'home': line[5], 'shell': line[6]}
        cnt += 1
    return users