def process_request(self, request):
    use_jwt_cookie_requested = request.META.get(USE_JWT_COOKIE_HEADER)
    header_payload_cookie = request.COOKIES.get(jwt_cookie_header_payload_name
        ())
    signature_cookie = request.COOKIES.get(jwt_cookie_signature_name())
    if not use_jwt_cookie_requested:
        metric_value = 'not-requested'
    elif header_payload_cookie and signature_cookie:
        request.COOKIES[jwt_cookie_name()] = '{}{}{}'.format(
            header_payload_cookie, JWT_DELIMITER, signature_cookie)
        metric_value = 'success'
    elif header_payload_cookie or signature_cookie:
        if not header_payload_cookie:
            log_message, metric_value = (self.
                _get_missing_cookie_message_and_metric(
                jwt_cookie_header_payload_name()))
        if not signature_cookie:
            log_message, metric_value = (self.
                _get_missing_cookie_message_and_metric(
                jwt_cookie_signature_name()))
        log.warning(log_message)
    else:
        metric_value = 'missing-both'
    monitoring.set_custom_metric('request_jwt_cookie', metric_value)