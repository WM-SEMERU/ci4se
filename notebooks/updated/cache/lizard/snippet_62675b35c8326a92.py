def ServicesGet(self, sensor_id):
    if self.__SenseApiCall__('/sensors/{0}/services.json'.format(sensor_id),
        'GET'):
        return True
    else:
        self.__error__ = 'api call unsuccessful'
        return False