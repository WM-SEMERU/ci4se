def is_valid_geometry(self):
    has_sites = (self.sites is not None or 'sites' in self.inputs or 
        'site_model' in self.inputs)
    if not has_sites and not self.ground_motion_fields:
        return True
    if 'gmfs' in self.inputs and not has_sites and not self.inputs['gmfs'
        ].endswith('.xml'):
        raise ValueError('Missing sites or sites_csv in the .ini file')
    elif 'risk' in self.calculation_mode or 'damage' in self.calculation_mode or 'bcr' in self.calculation_mode:
        return True
    flags = dict(sites=bool(self.sites), sites_csv=self.inputs.get('sites',
        0), hazard_curves_csv=self.inputs.get('hazard_curves', 0), gmfs_csv
        =self.inputs.get('gmfs', 0), region=bool(self.region and self.
        region_grid_spacing))
    return sum(bool(v) for v in flags.values()) == 1 or self.inputs.get(
        'exposure') or self.inputs.get('site_model')