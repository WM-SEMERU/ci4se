def delete(identifier, files=None, formats=None, glob_pattern=None,
    cascade_delete=None, access_key=None, secret_key=None, verbose=None,
    debug=None, **kwargs):
    files = get_files(identifier, files, formats, glob_pattern, **kwargs)
    responses = []
    for f in files:
        r = f.delete(cascade_delete=cascade_delete, access_key=access_key,
            secret_key=secret_key, verbose=verbose, debug=debug)
        responses.append(r)
    return responses