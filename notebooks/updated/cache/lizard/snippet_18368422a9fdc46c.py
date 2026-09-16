def list_types(self):
    uri = '/notification_types'
    resp, resp_body = self.api.method_get(uri)
    return [CloudMonitorNotificationType(self, info) for info in resp_body[
        'values']]