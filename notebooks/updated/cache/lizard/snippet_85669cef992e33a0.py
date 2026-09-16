def DeviceSensorsGet(self, device_id, parameters):
    if self.__SenseApiCall__('/devices/{0}/sensors.json'.format(device_id),
        'GET', parameters=parameters):
        return True
    else:
        self.__error__ = 'api call unsuccessful'
        return False