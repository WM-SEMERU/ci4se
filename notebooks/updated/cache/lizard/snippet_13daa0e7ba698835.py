def folder_name(self):
    name = self.site_packages_name
    if name is None:
        name = self.name
    return name