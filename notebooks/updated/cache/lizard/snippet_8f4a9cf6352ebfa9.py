def make_pilothole_cutter(self):
    pilothole_radius = self.pilothole_radius
    if pilothole_radius is None:
        inner_radius, outer_radius = self.get_radii()
        pilothole_radius = inner_radius + self.pilothole_ratio * (outer_radius
             - inner_radius)
    return cadquery.Workplane('XY').circle(pilothole_radius).extrude(self.
        length)