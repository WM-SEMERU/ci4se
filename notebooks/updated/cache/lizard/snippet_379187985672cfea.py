def _build_error_report(self, message, report_location=None, http_context=
    None, user=None):
    payload = {'serviceContext': {'service': self.service}, 'message':
        '{0}'.format(message)}
    if self.version:
        payload['serviceContext']['version'] = self.version
    if report_location or http_context or user:
        payload['context'] = {}
    if report_location:
        payload['context']['reportLocation'] = report_location
    if http_context:
        http_context_dict = http_context.__dict__
        payload['context']['httpRequest'] = {key: value for key, value in
            six.iteritems(http_context_dict) if value is not None}
    if user:
        payload['context']['user'] = user
    return payload