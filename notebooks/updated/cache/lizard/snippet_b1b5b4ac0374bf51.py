def prepare(data):
    sha = data.get('sha')
    tree = data.get('tree')
    return {'sha': sha, 'tree': tree}