def process_added_port(self, device_details):
    device = device_details['device']
    port_id = device_details['port_id']
    reprocess = True
    try:
        self._process_added_port(device_details)
        LOG.debug('Updating cached port %s status as UP.', port_id)
        self._update_port_status_cache(device, device_bound=True)
        LOG.info('Port %s processed.', port_id)
    except os_win_exc.HyperVvNicNotFound:
        LOG.debug('vNIC %s not found. This can happen if the VM was destroyed.'
            , port_id)
        reprocess = False
    except os_win_exc.HyperVPortNotFoundException:
        LOG.debug(
            'vSwitch port %s not found. This can happen if the VM was destroyed.'
            , port_id)
    except Exception as ex:
        LOG.exception(
            'Exception encountered while processing port %(port_id)s. Exception: %(ex)s'
            , dict(port_id=port_id, ex=ex))
    else:
        reprocess = False
    if reprocess:
        self._added_ports.add(device)
        self._refresh_cache = True
        return False
    return True