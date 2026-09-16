def url_download(url, topath=None, create_dirs=True):
    if topath:
        topath = os.path.expanduser(os.path.expandvars(topath))
    if create_dirs and topath:
        dnm = os.path.dirname(topath)
        if not os.path.isdir(dnm):
            os.makedirs(os.path.abspath(dnm), 493)
    if six.PY2:
        response = urllib.request.urlopen(url)
        if topath is None:
            topath = response.read()
        else:
            with open(topath, 'wb') as fl:
                shutil.copyfileobj(response, fl)
    else:
        with urllib.request.urlopen(url) as response:
            if topath is None:
                topath = response.read()
            else:
                with open(topath, 'wb') as fl:
                    shutil.copyfileobj(response, fl)
    return topath