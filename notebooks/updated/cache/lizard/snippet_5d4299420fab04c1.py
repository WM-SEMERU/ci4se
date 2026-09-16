def show_service_profile(self, flavor_profile, **_params):
    return self.get(self.service_profile_path % flavor_profile, params=_params)