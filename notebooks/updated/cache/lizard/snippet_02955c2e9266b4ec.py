def filter(self, data, range_obj):
    if isinstance(range_obj, (pd.DatetimeIndex, tuple)):
        range_obj = DateRange(range_obj[0], range_obj[-1])
    range_obj = to_pandas_closed_closed(range_obj, add_tz=False)
    start = range_obj.start
    end = range_obj.end
    if 'date' in data.index.names:
        return data[start:end]
    elif 'date' in data.columns:
        if start and end:
            return data[(data.date >= start) & (data.date <= end)]
        elif start:
            return data[data.date >= start]
        elif end:
            return data[data.date <= end]
        else:
            return data
    else:
        return data