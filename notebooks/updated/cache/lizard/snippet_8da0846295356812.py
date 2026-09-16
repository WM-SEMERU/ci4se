def GroupsSensorsDelete(self, group_id, sensor_id):
    if self.__SenseApiCall__('/groups/{0}/sensors/{1}.json'.format(group_id,
        sensor_id), 'DELETE'):
        return True
    else:
        self.__error__ = 'api call unsuccessful'
        return False