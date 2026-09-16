def handle_request_parsing_error(err, _req, _schema, _err_status_code,
    _err_headers):
    abort(HTTPStatus.BAD_REQUEST, errors=err.messages)