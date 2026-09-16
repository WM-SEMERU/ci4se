def ServicesGetMetod(self, sensor_id, service_id, method):
    if self.__SenseApiCall__('/sensors/{0}/services/{1}/{2}.json'.format(
        sensor_id, service_id, method), 'GET'):
        return True
    else:
        self.__error__ = 'api call unsuccessful'
        return False