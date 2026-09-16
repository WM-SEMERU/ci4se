def clear_branding(self):
    if self.get_branding_metadata().is_read_only(
        ) or self.get_branding_metadata().is_required():
        raise NoAccess()
    self.my_osid_object_form._my_map['brandingIds'] = self._branding_default