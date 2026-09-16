def add_site(self, site_name, location_name=None, er_data=None, pmag_data=None
    ):
    if location_name:
        location = self.find_by_name(location_name, self.locations)
        if not location:
            location = self.add_location(location_name)
    else:
        location = None
    new_site = Site(site_name, location, self.data_model, er_data, pmag_data)
    self.sites.append(new_site)
    if location:
        location.sites.append(new_site)
    return new_site