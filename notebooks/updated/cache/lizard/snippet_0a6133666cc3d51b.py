def get_weather_forecast(self, place, unit=None):
    unit = unit if unit else self.unit
    response = self.get_weather_in(place, items=['item.forecast'], unit=unit)
    return response