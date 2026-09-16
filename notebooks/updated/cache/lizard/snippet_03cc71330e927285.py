def parse_JSON(self, JSON_string):
    if JSON_string is None:
        raise parse_response_error.ParseResponseError('JSON data is None')
    d = json.loads(JSON_string)
    if 'message' in d and 'cod' in d:
        if d['cod'] == '404':
            print('OWM API: data not found - response payload: ' + json.
                dumps(d))
            return None
        elif d['cod'] != '200':
            raise api_response_error.APIResponseError(
                'OWM API: error - response payload: ' + json.dumps(d), d['cod']
                )
    if 'cnt' in d and d['cnt'] == '0':
        return []
    elif 'list' in d:
        try:
            return [weather.weather_from_dictionary(item) for item in d['list']
                ]
        except KeyError:
            raise parse_response_error.ParseResponseError(''.join([__name__,
                ': impossible to read weather info from JSON data']))
    else:
        raise parse_response_error.ParseResponseError(''.join([__name__,
            ': impossible to read weather list from JSON data']))