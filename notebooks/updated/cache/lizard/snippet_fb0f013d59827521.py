def _check_response_code(response, codes):
    if type(codes) == int:
        codes = [codes]
    if response.status_code not in codes:
        raise FireCloudServerError(response.status_code, response.content)