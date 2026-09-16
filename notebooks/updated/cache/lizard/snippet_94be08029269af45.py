def iter_orgs(username, number=-1, etag=None):
    return gh.iter_orgs(username, number, etag) if username else []