def current_consumption(self):
    res = 'N/A'
    if self.use_legacy_protocol:
        try:
            res = self.fetchMyCgi()['Meter Watt']
        except:
            return 'N/A'
    else:
        try:
            res = self.SOAPAction('GetCurrentPowerConsumption',
                'CurrentConsumption', self.moduleParameters('2'))
        except:
            return 'N/A'
    if res is None:
        return 'N/A'
    try:
        res = float(res)
    except ValueError:
        _LOGGER.error(
            'Failed to retrieve current power consumption from SmartPlug')
    return res