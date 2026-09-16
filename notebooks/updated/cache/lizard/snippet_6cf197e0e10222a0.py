def from_response(response, url):
    try:
        data = response.json()
        if not isinstance(data, dict):
            return from_status(response.status_code, response.text, extra=
                dict(url=url, response=response.text))
        code = data.get('code', response.status_code)
        if code in HTTP_STATUS_CODES:
            return HTTP_STATUS_CODES[code](**ErrorSchema().load(data))
        else:
            return Error(**ErrorSchema().load(data))
    except Exception:
        return from_status(response.status_code, response.text, extra=dict(
            url=url, response=response.text))