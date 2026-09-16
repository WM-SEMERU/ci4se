def get_extra_vehicle_info(self, authentication_info):
    import requests
    base_url = 'https://secure.ritassist.nl/GenericServiceJSONP.ashx'
    query = (
        '?f=CheckExtraVehicleInfo&token={token}&equipmentId={identifier}&lastHash=null&padding=false'
        )
    parameters = {'token': authentication_info.access_token, 'identifier':
        str(self.identifier)}
    response = requests.get(base_url + query.format(**parameters))
    json = response.json()
    self.malfunction_light = json['MalfunctionIndicatorLight']
    self.fuel_level = json['FuelLevel']
    self.coolant_temperature = json['EngineCoolantTemperature']
    self.power_voltage = json['PowerVoltage']