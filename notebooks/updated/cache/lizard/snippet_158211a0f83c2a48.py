def getContainerByTag(tag):
    require_str('tag', tag)
    container = None
    try:
        container = client.containers.get(tag)
        print('Found container', tag, '...')
    except NotFound:
        pass
    except APIError as exc:
        eprint('Unhandled error while getting container', tag)
        raise exc
    return container