def conda_prefix():
    try:
        out = subprocess.check_output(['conda', 'info', '--json'])
        return json.loads(out.decode())['default_prefix']
    except (subprocess.CalledProcessError, json.JSONDecodeError, OSError):
        return False