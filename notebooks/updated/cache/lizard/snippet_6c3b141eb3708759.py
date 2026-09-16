def get_flights_from_to(self, origin, destination):
    url = AIRLINE_FLT_BASE_POINTS.format(origin, destination)
    return self._fr24.get_airline_flight_data(url, by_airports=True)