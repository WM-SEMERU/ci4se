def update_recent_paths(response, path):
    try:
        recent_paths = environ.configs.fetch('recent_paths', [])
        if path in recent_paths:
            recent_paths.remove(path)
        recent_paths.insert(0, path)
        environ.configs.put(recent_paths=recent_paths[:10], persists=True)
        environ.configs.save()
    except Exception as error:
        response.warn(code='FAILED_RECENT_UPDATE', message=
            'Unable to update recently opened projects', error=str(error)
            ).console(whitespace=1)
    return True