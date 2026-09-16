def load_env_file():
    if not os.path.exists(ENV_FILE):
        return
    for line in open(ENV_FILE, 'r'):
        line = line.strip()
        if not line:
            continue
        name, value = line.split('=', 1)
        if not name or not value or name.startswith('#') or len(name
            ) == 0 or name.isspace():
            continue
        if re.match('^(["\\\']).*\\1$', value):
            if value.startswith('"'):
                value = os.path.expandvars(value)
            value = value[1:-1]
        os.environ[name] = value