def geocode(self, commit=False, force=False):
    if self.need_geocoding() or force:
        result = get_cached(getattr(self, self.geocoded_by), provider='google')
        if result.status == 'OK':
            for attribute, components in self.required_address_components.items(
                ):
                for component in components:
                    if not getattr(self, attribute) or force:
                        attr_val = getattr(result, component, None)
                        if attr_val:
                            setattr(self, attribute, attr_val)
        if commit:
            self.save()