def os_workload_status(configs, required_interfaces, charm_func=None):

    def wrap(f):

        @wraps(f)
        def wrapped_f(*args, **kwargs):
            f(*args, **kwargs)
            set_os_workload_status(configs, required_interfaces, charm_func)
        return wrapped_f
    return wrap