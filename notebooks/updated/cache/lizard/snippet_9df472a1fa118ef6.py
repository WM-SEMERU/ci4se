def read_env(path=None, environ=None, recurse=True):
    environ = environ if environ is not None else os.environ
    if path is None:
        frame = inspect.currentframe().f_back
        caller_dir = os.path.dirname(frame.f_code.co_filename)
        path = os.path.join(os.path.abspath(caller_dir), ENV)
    if recurse:
        current = path
        pardir = os.path.abspath(os.path.join(current, os.pardir))
        while current != pardir:
            target = os.path.join(current, ENV)
            if os.path.exists(target):
                path = os.path.abspath(target)
                break
            else:
                current = os.path.abspath(os.path.join(current, os.pardir))
                pardir = os.path.abspath(os.path.join(current, os.pardir))
        if not path:
            raise FileNotFoundError('Could not find a .env file')
    with open(path, 'r') as fp:
        content = fp.read()
    parsed = parse_env(content)
    for key, value in parsed.items():
        environ.setdefault(key, value)