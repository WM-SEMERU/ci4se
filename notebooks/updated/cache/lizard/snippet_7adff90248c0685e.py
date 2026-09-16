def get_msw(requestURL):
    msw_response = requests.get(requestURL)
    msw_response.raise_for_status()
    json_d = msw_response.json()
    headers = msw_response.headers
    if ERROR_RESPONSE in json_d:
        code = json_d.get(ERROR_RESPONE).get('code')
        msg = json_d.get(ERROR_RESPONE).get('error_msg')
        raise Exception('API returned error code {}. {}'.format(code, msg))
    if len(json_d) == 1:
        return ForecastDataPoint(json_d[0], headers, msw_response)
    return ForecastDataBlock(json_d, headers, msw_response)