def _parse(self, date_str, format='%Y-%m-%d'):
    rv = pd.to_datetime(date_str, format=format)
    if hasattr(rv, 'to_pydatetime'):
        rv = rv.to_pydatetime()
    return rv