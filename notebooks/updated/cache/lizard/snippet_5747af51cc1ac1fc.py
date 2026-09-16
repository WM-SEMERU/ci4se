def should_transform(self):
    if not HAS_DIAZO:
        self.log.info('HAS_DIAZO: false')
        return False
    if asbool(self.request.META.get(DIAZO_OFF_REQUEST_HEADER)):
        self.log.info('DIAZO_OFF_REQUEST_HEADER in request.META: off')
        return False
    if asbool(self.response.get(DIAZO_OFF_RESPONSE_HEADER)):
        self.log.info('DIAZO_OFF_RESPONSE_HEADER in response.get: off')
        return False
    if self.request.is_ajax():
        self.log.info('Request is AJAX')
        return False
    if self.response.streaming:
        self.log.info('Response has streaming')
        return False
    content_type = self.response.get('Content-Type')
    if not is_html_content_type(content_type):
        self.log.info('Content-type: false')
        return False
    content_encoding = self.response.get('Content-Encoding')
    if content_encoding in ('zip', 'compress'):
        self.log.info('Content encode is %s', content_encoding)
        return False
    status_code = str(self.response.status_code)
    if status_code.startswith('3'
        ) or status_code == '204' or status_code == '401':
        self.log.info('Status code: %s', status_code)
        return False
    if len(self.response.content) == 0:
        self.log.info('Response Content is EMPTY')
        return False
    self.log.info('Transform')
    return True