def find_geometry(self, physics):
    r
    if 'geometry' in physics.settings.keys():
        geom = self.geometries()[physics.settings['geometry']]
        return geom
    for geo in self.geometries().values():
        if physics in self.find_physics(geometry=geo):
            return geo
    raise Exception('Cannot find a geometry associated with ' + physics.name)