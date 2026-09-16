def SensorsDataGet(self, sensorIds, parameters):
    if parameters is None:
        parameters = {}
    parameters['sensor_id[]'] = sensorIds
    if self.__SenseApiCall__('/sensors/data.json', 'GET', parameters=parameters
        ):
        return True
    else:
        self.__error__ = 'api call unsuccessful'
        return False