def get_dates(self, request):
    if DataSource.is_timeless(request.data_source):
        return [None]
    date_interval = parse_time_interval(request.time)
    LOGGER.debug('date_interval=%s', date_interval)
    if request.wfs_iterator is None:
        self.wfs_iterator = WebFeatureService(request.bbox, date_interval,
            data_source=request.data_source, maxcc=request.maxcc, base_url=
            self.base_url, instance_id=self.instance_id)
    else:
        self.wfs_iterator = request.wfs_iterator
    dates = sorted(set(self.wfs_iterator.get_dates()))
    if request.time is OgcConstants.LATEST:
        dates = dates[-1:]
    return OgcService._filter_dates(dates, request.time_difference)