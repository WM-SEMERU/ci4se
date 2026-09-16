def log(package):
    team, owner, pkg = parse_package(package)
    session = _get_session(team)
    response = session.get('{url}/api/log/{owner}/{pkg}/'.format(url=
        get_registry_url(team), owner=owner, pkg=pkg))
    table = [('Hash', 'Pushed', 'Author', 'Tags', 'Versions')]
    for entry in reversed(response.json()['logs']):
        ugly = datetime.fromtimestamp(entry['created'])
        nice = ugly.strftime('%Y-%m-%d %H:%M:%S')
        table.append((entry['hash'], nice, entry['author'], str(entry.get(
            'tags', [])), str(entry.get('versions', []))))
    _print_table(table)