def init_environment():
    base_path = os.path.abspath(os.path.dirname(__file__))
    env_path = '{0}/.env'.format(base_path)
    if os.path.exists(env_path):
        with open(env_path) as f:
            lines = f.readlines()
            for line in lines:
                var = line.strip().split('=')
                if len(var) == 2:
                    os.environ[var[0]] = var[1]