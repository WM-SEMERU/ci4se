def build_sensors_list(self, type):
    ret = []
    if type == SENSOR_TEMP_UNIT and self.init_temp:
        input_list = self.stemps
        self.stemps = psutil.sensors_temperatures()
    elif type == SENSOR_FAN_UNIT and self.init_fan:
        input_list = self.sfans
        self.sfans = psutil.sensors_fans()
    else:
        return ret
    for chipname, chip in iteritems(input_list):
        i = 1
        for feature in chip:
            sensors_current = {}
            if feature.label == '':
                sensors_current['label'] = chipname + ' ' + str(i)
            else:
                sensors_current['label'] = feature.label
            sensors_current['value'] = int(feature.current)
            sensors_current['unit'] = type
            ret.append(sensors_current)
            i += 1
    return ret