def setup_dirs():
    try:
        top_dir = os.path.abspath(os.path.expanduser(os.environ[
            'XDG_CACHE_HOME']))
    except KeyError:
        top_dir = os.path.abspath(os.path.expanduser('~/.cache'))
    our_cache_dir = os.path.join(top_dir, PROJECT_NAME)
    os.makedirs(our_cache_dir, mode=509, exist_ok=True)
    return our_cache_dir