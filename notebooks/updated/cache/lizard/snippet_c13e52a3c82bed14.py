def get_devices(self):
    devices = self.make_request('["{username}","{password}","info","",""]'.
        format(username=self.username, password=self.password))
    if devices != False:
        garage_doors = []
        try:
            self.apicode = devices.find('apicode').text
            self._device_states = {}
            for doorNum in range(1, 4):
                door = devices.find('door' + str(doorNum))
                doorName = door.find('name').text
                if doorName:
                    dev = {'door': doorNum, 'name': doorName}
                    for id in ['mode', 'sensor', 'status', 'sensorid',
                        'temperature', 'voltage', 'camera', 'events',
                        'permission']:
                        item = door.find(id)
                        if item is not None:
                            dev[id] = item.text
                    garage_state = door.find('status').text
                    dev['status'] = self.DOOR_STATE[garage_state]
                    self._device_states[doorNum] = self.DOOR_STATE[garage_state
                        ]
                    garage_doors.append(dev)
            return garage_doors
        except TypeError as ex:
            print(ex)
            return False
    else:
        return False