def get_github_hostname_user_repo_from_url(url):
    parsed = parse.urlparse(url)
    if parsed.netloc == '':
        host, sep, path = parsed.path.partition(':')
        if '@' in host:
            username, sep, host = host.partition('@')
    else:
        path = parsed.path[1:].rstrip('/')
        host = parsed.netloc
    user, repo = path.split('/', 1)
    return host, user, repo[:-4] if repo.endswith('.git') else repo