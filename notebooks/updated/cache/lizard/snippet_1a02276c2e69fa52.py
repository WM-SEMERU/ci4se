def _dbdir():
    global dbdir
    from os import mkdir, path, getcwd, chdir
    if dbdir is None:
        from acorn.config import settings
        config = settings('acorn')
        if config.has_section('database') and config.has_option('database',
            'folder'):
            dbdir = config.get('database', 'folder')
        else:
            raise ValueError(
                "The folder to save DBs in must be configured  in 'acorn.cfg'")
    from acorn.utility import abspath
    if not path.isabs(dbdir):
        dbdir = abspath(dbdir)
    if not path.isdir(dbdir):
        mkdir(dbdir)
    return dbdir