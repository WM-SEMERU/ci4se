def clear():
    try:
        os.remove(os.path.join(__opts__['cachedir'], 'datastore'))
    except (IOError, OSError):
        pass
    return True