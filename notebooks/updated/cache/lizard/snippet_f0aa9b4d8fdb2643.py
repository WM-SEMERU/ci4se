def _return_parsed_timezone_results(result, timezones, box, tz, name):
    if tz is not None:
        raise ValueError(
            'Cannot pass a tz argument when parsing strings with timezone information.'
            )
    tz_results = np.array([Timestamp(res).tz_localize(zone) for res, zone in
        zip(result, timezones)])
    if box:
        from pandas import Index
        return Index(tz_results, name=name)
    return tz_results