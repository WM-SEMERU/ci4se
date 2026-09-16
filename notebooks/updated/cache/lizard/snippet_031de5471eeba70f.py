def daily_forecast(self, name, limit=None):
    assert isinstance(name, str), 'Value must be a string'
    encoded_name = name
    if limit is not None:
        assert isinstance(limit, int), "'limit' must be an int or None"
        if limit < 1:
            raise ValueError("'limit' must be None or greater than zero")
    params = {'q': encoded_name, 'lang': self._language}
    if limit is not None:
        params['cnt'] = limit
    uri = http_client.HttpClient.to_url(DAILY_FORECAST_URL, self._API_key,
        self._subscription_type, self._use_ssl)
    _, json_data = self._wapi.cacheable_get_json(uri, params=params)
    forecast = self._parsers['forecast'].parse_JSON(json_data)
    if forecast is not None:
        forecast.set_interval('daily')
        return forecaster.Forecaster(forecast)
    else:
        return None