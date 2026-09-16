def to_json(self):
    return {'name': self.name, 'day_type': self.day_type, 'location': self.
        location.to_json(), 'dry_bulb_condition': self.dry_bulb_condition.
        to_json(), 'humidity_condition': self.humidity_condition.to_json(),
        'wind_condition': self.wind_condition.to_json(), 'sky_condition':
        self.sky_condition.to_json()}