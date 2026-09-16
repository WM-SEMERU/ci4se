def GroupsSensorsGet(self, group_id, parameters):
    if self.__SenseApiCall('/groups/{0}/sensors.json'.format(group_id),
        'GET', parameters=parameters):
        return True
    else:
        self.__error__ = 'api call unsuccessful'
        return False