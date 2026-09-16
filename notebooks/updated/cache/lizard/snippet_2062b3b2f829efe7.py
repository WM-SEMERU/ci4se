def FetchMostRecentGraphSeries(label, report_type, token=None):
    if _ShouldUseLegacyDatastore():
        return _FetchMostRecentGraphSeriesFromTheLegacyDB(label,
            report_type, token=token)
    return data_store.REL_DB.ReadMostRecentClientGraphSeries(label, report_type
        )