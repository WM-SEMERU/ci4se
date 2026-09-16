def _sign_response(self, response):
    if 'Authorization' not in request.headers:
        return response
    try:
        mohawk_receiver = mohawk.Receiver(credentials_map=self.
            _client_key_loader_func, request_header=request.headers[
            'Authorization'], url=request.url, method=request.method,
            content=request.get_data(), content_type=request.mimetype,
            accept_untrusted_content=current_app.config[
            'HAWK_ACCEPT_UNTRUSTED_CONTENT'], localtime_offset_in_seconds=
            current_app.config['HAWK_LOCALTIME_OFFSET_IN_SECONDS'],
            timestamp_skew_in_seconds=current_app.config[
            'HAWK_TIMESTAMP_SKEW_IN_SECONDS'])
    except mohawk.exc.HawkFail:
        return response
    response.headers['Server-Authorization'] = mohawk_receiver.respond(content
        =response.data, content_type=response.mimetype)
    return response