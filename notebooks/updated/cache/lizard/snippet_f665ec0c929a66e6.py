def _CreateShapesFolder(self, schedule, doc):
    if not schedule.GetShapeList():
        return None
    shapes_folder = self._CreateFolder(doc, 'Shapes')
    shapes = list(schedule.GetShapeList())
    shapes.sort(key=lambda x: x.shape_id)
    for shape in shapes:
        placemark = self._CreatePlacemark(shapes_folder, shape.shape_id)
        self._CreateLineStringForShape(placemark, shape)
        if self.shape_points:
            self._CreateShapePointFolder(shapes_folder, shape)
    return shapes_folder