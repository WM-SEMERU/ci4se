def FetchAllGraphSeries(label, report_type, period=None, token=None):
    if _ShouldUseLegacyDatastore():
        return _FetchAllGraphSeriesFromTheLegacyDB(label, report_type,
            period=period, token=token)
    if period is None:
        time_range = None
    else:
        range_end = rdfvalue.RDFDatetime.Now()
        time_range = time_utils.TimeRange(range_end - period, range_end)
    return data_store.REL_DB.ReadAllClientGraphSeries(label, report_type,
        time_range=time_range)