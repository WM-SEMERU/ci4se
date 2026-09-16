def get_time_axis(start_time, end_time, time_step, time_axis=None):
    from ..lib import units
    if time_axis is not None:
        actual_dates_axis = []
        for t in time_axis:
            t = t.replace(',', '').strip()
            if t == '':
                continue
            actual_dates_axis.append(get_datetime(t))
        return actual_dates_axis
    else:
        if start_time is None:
            raise HydraPluginError('A start time must be specified')
        if end_time is None:
            raise HydraPluginError('And end time must be specified')
        if time_step is None:
            raise HydraPluginError('A time-step must be specified')
        start_date = get_datetime(start_time)
        end_date = get_datetime(end_time)
        delta_t, value, output_units = parse_time_step(time_step, units_ref
            =units)
        time_axis = [start_date]
        value = int(value)
        while start_date < end_date:
            if output_units.lower() == 'mon':
                start_date = start_date + relativedelta(months=value)
            elif output_units.lower() == 'yr':
                start_date = start_date + relativedelta(years=value)
            else:
                start_date += timedelta(seconds=delta_t)
            time_axis.append(start_date)
        return time_axis