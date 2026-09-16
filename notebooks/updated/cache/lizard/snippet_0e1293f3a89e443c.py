def configure(self, address):
    global nanoconfig_started
    if len(self._endpoints):
        raise ValueError('Nanoconfig address must be sole endpoint')
    endpoint_id = _nn_check_positive_rtn(wrapper.nc_configure(self.fd, address)
        )
    if not nanoconfig_started:
        nanoconfig_started = True
    ep = Socket.NanoconfigEndpoint(self, endpoint_id, address)
    self._endpoints.append(ep)
    return ep