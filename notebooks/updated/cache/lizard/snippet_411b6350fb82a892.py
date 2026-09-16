def getDetails(self, ip_address=None):
    raw_details = self._requestDetails(ip_address)
    raw_details['country_name'] = self.countries.get(raw_details.get('country')
        )
    raw_details['ip_address'] = ipaddress.ip_address(raw_details.get('ip'))
    raw_details['latitude'], raw_details['longitude'] = self._read_coords(
        raw_details.get('loc'))
    return Details(raw_details)