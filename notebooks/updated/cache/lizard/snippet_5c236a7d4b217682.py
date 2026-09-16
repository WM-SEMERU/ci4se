def get_network_disconnect_kwargs(self, action, network_name,
    container_name, kwargs=None):
    c_kwargs = dict(container=container_name, net_id=network_name)
    update_kwargs(c_kwargs, kwargs)
    return c_kwargs