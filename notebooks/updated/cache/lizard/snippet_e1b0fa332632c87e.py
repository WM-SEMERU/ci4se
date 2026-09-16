def geolocate(self, ip: str):
    url_path = '/api/geoloc/{ip}'.format(ip=ip)
    return self._request_without_api(path=url_path)