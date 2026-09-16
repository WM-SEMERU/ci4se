def make_simple(self):
    inner_radius, outer_radius = self.get_radii()
    radius = (inner_radius + outer_radius) / 2
    return cadquery.Workplane('XY').circle(radius).extrude(self.length)