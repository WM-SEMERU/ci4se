def merge_vertices(self, digits=None):
    if len(self.vertices) == 0:
        return
    if digits is None:
        digits = util.decimal_to_digits(tol.merge * self.scale, min_digits=1)
    unique, inverse = grouping.unique_rows(self.vertices, digits=digits)
    self.vertices = self.vertices[unique]
    entities_ok = np.ones(len(self.entities), dtype=np.bool)
    for index, entity in enumerate(self.entities):
        kind = type(entity).__name__
        if kind in 'BSpline Bezier Text':
            entity.points = inverse[entity.points]
            continue
        points = grouping.merge_runs(inverse[entity.points])
        if kind == 'Line':
            if len(points) == 3 and points[0] == points[-1]:
                points = points[:2]
            elif len(points) < 2:
                entities_ok[index] = False
        elif kind == 'Arc' and len(points) != 3:
            entities_ok[index] = False
        entity.points = points
    self.entities = self.entities[entities_ok]