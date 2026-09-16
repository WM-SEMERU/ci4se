def request(self, method, params, session):
    session = session or self.client.session
    request = self.create_req(method, params)
    date_time_sent = datetime.datetime.utcnow()
    try:
        response = session.post(self.url, data=request, headers=self.client
            .request_headers, timeout=(self.connect_timeout, self.read_timeout)
            )
    except ConnectionError:
        raise APIError(None, method, params, 'ConnectionError')
    except Exception as e:
        raise APIError(None, method, params, e)
    elapsed_time = (datetime.datetime.utcnow() - date_time_sent).total_seconds(
        )
    check_status_code(response)
    try:
        response_data = response.json()
    except ValueError:
        raise InvalidResponse(response.text)
    if self._error_handler:
        self._error_handler(response_data, method, params)
    return response_data, elapsed_time