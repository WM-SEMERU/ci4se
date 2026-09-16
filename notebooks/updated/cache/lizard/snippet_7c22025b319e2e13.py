def get_tstat(self, site, start, end, var='tstat_temp', agg='MEAN', window=
    '24h', aligned=True, return_names=True):
    start = self.convert_to_utc(start)
    end = self.convert_to_utc(end)
    point_map = {'tstat_state': 'Thermostat_Status', 'tstat_hsp':
        'Supply_Air_Temperature_Heating_Setpoint', 'tstat_csp':
        'Supply_Air_Temperature_Cooling_Setpoint', 'tstat_temp':
        'Temperature_Sensor'}
    if isinstance(var, list):
        point_type = [point_map[point_type] for point_type in var]
    else:
        point_type = point_map[var]
    request = self.compose_MDAL_dic(point_type=point_type, site=site, start
        =start, end=end, var=var, agg=agg, window=window, aligned=aligned)
    resp = self.m.query(request)
    if return_names:
        resp = self.replace_uuid_w_names(resp)
    return resp