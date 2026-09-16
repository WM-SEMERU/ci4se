def get_container_stop_kwargs(self, action, container_name, kwargs=None):
    c_kwargs = dict(container=container_name)
    stop_timeout = action.config.stop_timeout
    if stop_timeout is NotSet:
        timeout = action.client_config.get('stop_timeout')
        if timeout is not None:
            c_kwargs['timeout'] = timeout
    elif stop_timeout is not None:
        c_kwargs['timeout'] = stop_timeout
    update_kwargs(c_kwargs, kwargs)
    return c_kwargs