def distance(self, there):
    return haversine_distance((self.latitude, self.longitude), (there.
        latitude, there.longitude))