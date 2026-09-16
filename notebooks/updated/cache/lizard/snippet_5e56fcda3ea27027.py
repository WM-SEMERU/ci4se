def load_env(keys=[], name='NT', use_getpass=False):
    NT = namedtuple(name, keys)
    if use_getpass:
        values = [(os.getenv(x) or getpass.getpass(x)) for x in keys]
    else:
        values = [(os.getenv(x) or input(x)) for x in keys]
    return NT(*values)