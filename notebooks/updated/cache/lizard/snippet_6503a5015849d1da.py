def discover():
    _append_path(hookenv.charm_dir())
    _append_path(os.path.join(hookenv.charm_dir(), 'hooks'))
    for search_dir in ('reactive', 'hooks/reactive', 'hooks/relations'):
        search_path = os.path.join(hookenv.charm_dir(), search_dir)
        for dirpath, dirnames, filenames in os.walk(search_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                _register_handlers_from_file(search_path, filepath)