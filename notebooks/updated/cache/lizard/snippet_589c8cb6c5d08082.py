def _treat_devices_added(self):
    try:
        devices_details_list = self._plugin_rpc.get_devices_details_list(self
            ._context, self._added_ports, self._agent_id)
    except Exception as exc:
        LOG.debug(
            'Unable to get ports details for devices %(devices)s: %(exc)s',
            {'devices': self._added_ports, 'exc': exc})
        return
    for device_details in devices_details_list:
        device = device_details['device']
        LOG.info('Adding port %s', device)
        if 'port_id' in device_details:
            LOG.info('Port %(device)s updated. Details: %(device_details)s',
                {'device': device, 'device_details': device_details})
            eventlet.spawn_n(self.process_added_port, device_details)
        else:
            LOG.debug(
                'Missing port_id from device details: %(device)s. Details: %(device_details)s'
                , {'device': device, 'device_details': device_details})
        LOG.debug(
            "Remove the port from added ports set, so it doesn't get reprocessed."
            )
        self._added_ports.discard(device)