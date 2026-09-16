def give_satellite_json(self):
    daemon_properties = ['type', 'name', 'uri', 'spare',
        'configuration_sent', 'realm_name', 'manage_sub_realms', 'active',
        'reachable', 'alive', 'passive', 'last_check', 'polling_interval',
        'max_check_attempts']
    livestate, livestate_output = self.get_livestate()
    res = {'livestate': livestate, 'livestate_output': livestate_output}
    for sat_prop in daemon_properties:
        res[sat_prop] = getattr(self, sat_prop, 'not_yet_defined')
    return res