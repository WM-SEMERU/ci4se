def bottom_grain(self):
    bottom_sites = []
    for i, tag in enumerate(self.site_properties['grain_label']):
        if 'bottom' in tag:
            bottom_sites.append(self.sites[i])
    return Structure.from_sites(bottom_sites)