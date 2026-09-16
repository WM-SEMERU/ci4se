def get_ride_types(self, latitude, longitude, ride_type=None):
    args = OrderedDict([('lat', latitude), ('lng', longitude), ('ride_type',
        ride_type)])
    return self._api_call('GET', 'v1/ridetypes', args=args)