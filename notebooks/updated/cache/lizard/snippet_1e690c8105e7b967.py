def get(self, sensor_type='temperature_core'):
    self.__update__()
    if sensor_type == 'temperature_core':
        ret = [s for s in self.sensors_list if s['unit'] == SENSOR_TEMP_UNIT]
    elif sensor_type == 'fan_speed':
        ret = [s for s in self.sensors_list if s['unit'] == SENSOR_FAN_UNIT]
    else:
        logger.debug('Unknown sensor type %s' % sensor_type)
        ret = []
    return ret