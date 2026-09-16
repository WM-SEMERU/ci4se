def get_forecast_sites(self):
    time_now = time()
    if (time_now - self.forecast_sites_last_update > self.
        forecast_sites_update_time or self.forecast_sites_last_request is None
        ):
        data = self.__call_api('sitelist/')
        sites = list()
        for jsoned in data['Locations']['Location']:
            site = Site()
            site.name = jsoned['name']
            site.id = jsoned['id']
            site.latitude = jsoned['latitude']
            site.longitude = jsoned['longitude']
            if 'region' in jsoned:
                site.region = jsoned['region']
            if 'elevation' in jsoned:
                site.elevation = jsoned['elevation']
            if 'unitaryAuthArea' in jsoned:
                site.unitaryAuthArea = jsoned['unitaryAuthArea']
            if 'nationalPark' in jsoned:
                site.nationalPark = jsoned['nationalPark']
            site.api_key = self.api_key
            sites.append(site)
        self.forecast_sites_last_request = sites
        self.forecast_sites_last_update = time_now
    else:
        sites = self.forecast_sites_last_request
    return sites