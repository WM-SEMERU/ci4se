def vault_file(env, default):
    home = os.environ['HOME'] if 'HOME' in os.environ else os.environ[
        'USERPROFILE']
    filename = os.environ.get(env, os.path.join(home, default))
    filename = abspath(filename)
    if os.path.exists(filename):
        return filename
    return None