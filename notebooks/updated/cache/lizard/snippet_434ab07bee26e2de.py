def GetElevation(self, LatLngSet, sensor=False):
    locations = []
    for [lat, lng] in LatLngSet:
        locations.append(str(lat) + ',' + str(lng))
    locations = '|'.join(locations)
    params = {'locations': locations, 'sensor': str(sensor).lower()}
    if not self.premier:
        url = self.get_url(params)
    else:
        url = self.get_signed_url(params)
    return self.GetService_url(url)