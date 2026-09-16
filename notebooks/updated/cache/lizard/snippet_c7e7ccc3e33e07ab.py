def metrics_api(self):
    if self._metrics_api is None:
        if self._use_grpc:
            self._metrics_api = _gapic.make_metrics_api(self)
        else:
            self._metrics_api = JSONMetricsAPI(self)
    return self._metrics_api