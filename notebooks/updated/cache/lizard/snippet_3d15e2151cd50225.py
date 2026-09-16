def pair_new_device(self, pairing_mode, pairing_mode_duration=60,
    pairing_device_type_selector=None, kidde_radio_code=None):
    if pairing_mode == 'lutron' and pairing_mode_duration < 120:
        pairing_mode_duration = 120
    elif pairing_mode == 'zwave_network_rediscovery':
        pairing_mode_duration = 0
    elif pairing_mode == 'bluetooth' and pairing_device_type_selector is None:
        pairing_device_type_selector = 'switchmate'
    desired_state = {'pairing_mode': pairing_mode, 'pairing_mode_duration':
        pairing_mode_duration}
    if pairing_mode == 'kidde' and kidde_radio_code is not None:
        try:
            kidde_radio_code_int = int(kidde_radio_code, 2)
            desired_state = {'kidde_radio_code': kidde_radio_code_int,
                'pairing_mode': None}
        except (TypeError, ValueError):
            _LOGGER.error('An invalid Kidde radio code was provided. %s',
                kidde_radio_code)
    if pairing_device_type_selector is not None:
        desired_state.update({'pairing_device_type_selector':
            pairing_device_type_selector})
    response = self.api_interface.set_device_state(self, {'desired_state':
        desired_state})
    self._update_state_from_response(response)