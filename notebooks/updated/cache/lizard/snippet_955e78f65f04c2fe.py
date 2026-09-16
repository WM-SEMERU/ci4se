def set_timezone(data, tz=None, from_local=False):
    if isinstance(data, pd.DataFrame) | isinstance(data, pd.Series):
        try:
            try:
                data.index = data.index.tz_convert(tz)
            except Exception as e:
                if from_local:
                    data.index = data.index.tz_localize(get_timezone()
                        ).tz_convert(tz)
                else:
                    data.index = data.index.tz_localize('UTC').tz_convert(tz)
        except Exception as e:
            pass
    else:
        if isinstance(data, str):
            data = parse_date(data)
        try:
            try:
                data = data.astimezone(tz)
            except Exception as e:
                data = timezone('UTC').localize(data).astimezone(timezone(tz))
        except Exception as e:
            pass
    return data