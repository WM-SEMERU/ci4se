def add_polyline(self, path=None, **kwargs):
    if path:
        if not isinstance(path, list):
            raise AttributeError(
                'The path is a list of dictionary oflatitude and longitudes por path points'
                )
        for i, point in enumerate(path):
            if not isinstance(point, dict):
                if isinstance(point, (list, tuple)) and len(point) == 2:
                    path[i] = {'lat': point[0], 'lng': point[1]}
                else:
                    raise AttributeError(
                        'All points in the path must be dicts of latitudes and longitudes, list or tuple'
                        )
        kwargs['path'] = path
    kwargs.setdefault('stroke_color', '#FF0000')
    kwargs.setdefault('stroke_opacity', 0.8)
    kwargs.setdefault('stroke_weight', 2)
    self.polylines.append(kwargs)