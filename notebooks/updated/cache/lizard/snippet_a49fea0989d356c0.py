def get_pull_request(project, num, auth=False):
    url = 'https://api.github.com/repos/{project}/pulls/{num}'.format(project
        =project, num=num)
    if auth:
        header = make_auth_header()
    else:
        header = None
    response = requests.get(url, headers=header)
    response.raise_for_status()
    return json.loads(response.text, object_hook=Obj)