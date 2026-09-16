def repositories(doc):
    for repository_id, repo in doc.get('repositories', {}).items():
        repo['id'] = repository_id
        repo['organisation_id'] = doc['_id']
        yield repository_id, repo