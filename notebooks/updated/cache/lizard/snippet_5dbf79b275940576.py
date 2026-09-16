def thermostat_states(self):
    return [ThermostatState(STATES[state.get('id')], state.get('id'), state
        .get('tempValue'), state.get('dhw')) for state in self._state[
        'thermostatStates']['state']]