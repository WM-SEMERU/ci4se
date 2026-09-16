def inverse(self):
    csg = self.clone()
    map(lambda p: p.flip(), csg.polygons)
    return csg