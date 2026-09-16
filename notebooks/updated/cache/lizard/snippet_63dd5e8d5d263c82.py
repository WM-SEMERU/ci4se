def draw_capitan_stroke_onto_canvas(self, export_path: ExportPath,
    stroke_thickness: int, margin: int):
    width = int(self.dimensions.width + 2 * margin)
    height = int(self.dimensions.height + 2 * margin)
    offset = Point2D(self.dimensions.origin.x - margin, self.dimensions.
        origin.y - margin)
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
    black = 0, 0, 0
    for i in range(0, len(self.stroke) - 1):
        start_point = self.__subtract_offset(self.stroke[i], offset)
        end_point = self.__subtract_offset(self.stroke[i + 1], offset)
        distance = self.__euclidean_distance(start_point, end_point)
        if distance > 1600:
            continue
        draw.line((start_point.x, start_point.y, end_point.x, end_point.y),
            black, stroke_thickness)
    del draw
    image.save(export_path.get_full_path())
    image.close()