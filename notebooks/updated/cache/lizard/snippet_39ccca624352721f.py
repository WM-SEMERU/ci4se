def _features_without_strokes(self, hwr_obj):
    x = []
    for point in hwr_obj.get_pointlist()[0]:
        if len(x) >= 3 * self.points_per_stroke or len(x
            ) >= 2 * self.points_per_stroke and not self.pen_down:
            break
        x.append(point['x'])
        x.append(point['y'])
        if self.pen_down:
            if 'pen_down' not in point:
                logging.error(
                    'The ConstantPointCoordinates(strokes=0) feature should only be used after SpaceEvenly preprocessing step.'
                    )
            else:
                x.append(int(point['pen_down']))
    if self.pen_down:
        while len(x) != 3 * self.points_per_stroke:
            x.append(self.fill_empty_with)
    else:
        while len(x) != 2 * self.points_per_stroke:
            x.append(self.fill_empty_with)
    return x