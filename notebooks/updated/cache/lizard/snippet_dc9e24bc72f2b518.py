def get_github_content(repo, path, auth=None):
    request = requests.get(file_url.format(repo=repo, path=path), auth=auth)
    if not request.ok:
        print('There is a problem with the request')
        print(file_url.format(repo=repo, path=path))
        print(request.json())
        exit(1)
    if not request.json()['encoding'] == 'base64':
        raise RuntimeError(
            'Unknown Encoding encountered when fetching {} from repo {}: {}'
            .format(path, repo, request.json()['encoding']))
    return request.json()['content'].decode('base64').decode('utf8')