def to_dict(self):
    identity_dict = {}
    if self.identity:
        identity_dict = self.identity.to_dict()
    json_dict = {'resourceId': self.resource_id, 'apiId': self.api_id,
        'resourcePath': self.resource_path, 'httpMethod': self.http_method,
        'requestId': self.request_id, 'accountId': self.account_id, 'stage':
        self.stage, 'identity': identity_dict, 'extendedRequestId': self.
        extended_request_id, 'path': self.path}
    return json_dict