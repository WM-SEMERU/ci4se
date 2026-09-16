def create_commit(profile, message, tree, parents):
    resource = '/commits'
    payload = {'message': message, 'tree': tree, 'parents': parents}
    data = api.post_request(profile, resource, payload)
    return prepare(data)