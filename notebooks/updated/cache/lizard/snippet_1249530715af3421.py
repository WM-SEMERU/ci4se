def thermostat_info(self):
    info = self._state['thermostatInfo']
    return ThermostatInfo(info.get('activeState'), info.get(
        'boilerModuleConnected'), info.get('burnerInfo'), info.get(
        'currentDisplayTemp'), info.get('currentModulationLevel'), info.get
        ('currentSetpoint'), info.get('currentTemp'), info.get('errorFound'
        ), info.get('haveOTBoiler'), info.get('nextProgram'), info.get(
        'nextSetpoint'), info.get('nextState'), info.get('nextTime'), info.
        get('otCommError'), info.get('programState'), info.get(
        'randomConfigId'), info.get('realSetpoint'))