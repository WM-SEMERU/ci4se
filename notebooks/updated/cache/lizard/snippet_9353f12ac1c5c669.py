def make_es_id(uri):
    try:
        uri = uri.clean_uri
    except AttributeError:
        pass
    return sha1(uri.encode()).hexdigest()