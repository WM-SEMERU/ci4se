def make_response(message, status_code, details=None):
    response_body = dict(message=message)
    if details:
        response_body['details'] = details
    response = jsonify(response_body)
    response.status_code = status_code
    return response