def set_siren_volume(self, volume):
    values = {'desired_state': {'siren_volume': volume}}
    response = self.api_interface.set_device_state(self, values)
    self._update_state_from_response(response)