def find_changed():
    session_token = request.headers['session_token']
    repository = request.headers['repository']
    current_user = have_authenticated_user(request.environ['REMOTE_ADDR'],
        repository, session_token)
    if current_user is False:
        return fail(user_auth_fail_msg)
    repository_path = config['repositories'][repository]['path']
    body_data = request.get_json()
    data_store = versioned_storage(repository_path)
    head = data_store.get_head()
    if head == 'root':
        return success({}, {'head': 'root', 'sorted_changes': {'none': []}})
    client_changes = json.loads(body_data['client_changes'])
    server_changes = data_store.get_changes_since(request.headers[
        'previous_revision'], head)
    conflict_resolutions = json.loads(body_data['conflict_resolutions'])
    if conflict_resolutions != []:
        resolutions = {'server': {}, 'client': {}}
        for r in conflict_resolutions:
            if len(r['4_resolution']) != 1 or r['4_resolution'][0] not in [
                'client', 'server']:
                return fail(conflict_msg)
            resolutions[r['4_resolution'][0]][r['1_path']] = None
        client_changes = {k: v for k, v in client_changes.iteritems() if v[
            'path'] not in resolutions['server']}
        server_changes = {k: v for k, v in server_changes.iteritems() if v[
            'path'] not in resolutions['client']}
    sorted_changes = merge_client_and_server_changes(server_changes,
        client_changes)
    return success({}, {'head': head, 'sorted_changes': sorted_changes})