def get_metric_data_points(self, metric, start, end, points=None,
    resolution=None, stats=None):
    return self._metrics_manager.get_metric_data_points(metric, start, end,
        points=points, resolution=resolution, stats=stats)