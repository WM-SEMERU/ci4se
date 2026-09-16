def _get_points_for_series(self, series):
    for point in series.get('values', []):
        yield self.point_from_cols_vals(series['columns'], point)