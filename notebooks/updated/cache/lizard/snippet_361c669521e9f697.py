def _set_dhw(self, status='Scheduled', mode=None, next_time=None):
    data = {'Status': status, 'Mode': mode, 'NextTime': next_time,
        'SpecialModes': None, 'HeatSetpoint': None, 'CoolSetpoint': None}
    self._populate_full_data()
    dhw_zone = self._get_dhw_zone()
    if dhw_zone is None:
        raise Exception('No DHW zone reported from API')
    url = (self.hostname + 
        '/WebAPI/api/devices/%s/thermostat/changeableValues' % dhw_zone)
    response = self._do_request('put', url, json.dumps(data))
    task_id = self._get_task_id(response)
    while self._get_task_status(task_id) != 'Succeeded':
        time.sleep(1)