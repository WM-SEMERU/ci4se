def error_class_for_http_status(status):
    try:
        return error_classes[status]
    except KeyError:

        def new_status_error(xml_response):
            if status > 400 and status < 500:
                return UnexpectedClientError(status, xml_response)
            if status > 500 and status < 600:
                return UnexpectedServerError(status, xml_response)
            return UnexpectedStatusError(status, xml_response)
        return new_status_error