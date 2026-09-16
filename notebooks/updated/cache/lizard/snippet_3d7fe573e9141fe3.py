def get_pickup_time_estimates(self, latitude, longitude, ride_type=None):
    args = OrderedDict([('lat', latitude), ('lng', longitude), ('ride_type',
        ride_type)])
    return self._api_call('GET', 'v1/eta', args=args)