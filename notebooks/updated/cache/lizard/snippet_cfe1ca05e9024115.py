def distance_between(self, place_1, place_2, unit='km'):
    pickled_place_1 = self._pickle(place_1)
    pickled_place_2 = self._pickle(place_2)
    try:
        return self.redis.geodist(self.key, pickled_place_1,
            pickled_place_2, unit=unit)
    except TypeError:
        return None