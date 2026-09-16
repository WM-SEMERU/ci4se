def set_fan_timer(self, timer):
    desired_state = {'timer': timer}
    resp = self.api_interface.set_device_state(self, {'desired_state':
        desired_state})
    self._update_state_from_response(resp)