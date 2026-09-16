def state_attributes(self):
    address_attributes = None
    if self.current_address is not None:
        address_attributes = self.current_address.state_attributes()
    return {'id': self.identifier, 'make': self.make, 'model': self.model,
        'license_plate': self.license_plate, 'active': self.active, 'odo':
        self.odo, 'latitude': self.latitude, 'longitude': self.longitude,
        'altitude': self.altitude, 'speed': self.speed, 'last_seen': self.
        last_seen, 'friendly_name': self.license_plate, 'equipment_id':
        self.equipment_id, 'fuel_level': self.fuel_level,
        'malfunction_light': self.malfunction_light, 'coolant_temperature':
        self.coolant_temperature, 'power_voltage': self.power_voltage,
        'current_max_speed': self.current_maximum_speed, 'current_address':
        address_attributes}