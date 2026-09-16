def _connect_mitogen_su(spec):
    return {'method': 'su', 'kwargs': {'username': spec.remote_user(),
        'password': spec.password(), 'python_path': spec.python_path(),
        'su_path': spec.become_exe(), 'connect_timeout': spec.timeout(),
        'remote_name': get_remote_name(spec)}}