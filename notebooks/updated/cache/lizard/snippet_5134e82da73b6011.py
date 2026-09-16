def need_geocoding(self):
    need_geocoding = False
    for attribute, component in self.required_address_components.items():
        if not getattr(self, attribute):
            need_geocoding = True
            break
    return need_geocoding