def get_state_in_ec_string(self, ec_index, add_colour=True):
    with self._mutex:
        if ec_index >= len(self.owned_ecs):
            ec_index -= len(self.owned_ecs)
            if ec_index >= len(self.participating_ecs):
                raise exceptions.BadECIndexError(ec_index)
            state = self.participating_ec_states[ec_index]
        else:
            state = self.owned_ec_states[ec_index]
    if state == self.INACTIVE:
        result = 'Inactive', ['bold', 'blue']
    elif state == self.ACTIVE:
        result = 'Active', ['bold', 'green']
    elif state == self.ERROR:
        result = 'Error', ['bold', 'white', 'bgred']
    elif state == self.UNKNOWN:
        result = 'Unknown', ['bold', 'red']
    elif state == self.CREATED:
        result = 'Created', ['reset']
    if add_colour:
        return utils.build_attr_string(result[1], supported=add_colour
            ) + result[0] + utils.build_attr_string('reset', supported=
            add_colour)
    else:
        return result[0]