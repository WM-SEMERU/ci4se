def format_users():
    lines = []
    u = users()
    count = u['count']
    if not count:
        raise DapiCommError('Could not find any users on DAPI.')
    for user in u['results']:
        line = user['username']
        if user['full_name']:
            line += ' (' + user['full_name'] + ')'
        lines.append(line)
    return lines