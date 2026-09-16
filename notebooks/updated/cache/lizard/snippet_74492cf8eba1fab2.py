def set_transition_time(self, transition_time):
    command = {ATTR_START_ACTION: {ATTR_DEVICE_STATE: self.state,
        ROOT_START_ACTION: [{ATTR_ID: self.raw[ATTR_ID], ATTR_LIGHT_DIMMER:
        self.raw[ATTR_LIGHT_DIMMER], ATTR_TRANSITION_TIME: transition_time *
        10 * 60}, self.devices_dict]}}
    return self.set_values(command)