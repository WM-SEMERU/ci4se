def _request_internal(self, command, **kwargs):
    args = dict(kwargs)
    if self.ssid:
        args['ssid'] = self.ssid
    method = getattr(self.api, command)
    response = method(**args)
    if response and 'status' in response:
        if response['status'] == 'error':
            raise SubregError(message=response['error']['errormsg'], major=
                response['error']['errorcode']['major'], minor=response[
                'error']['errorcode']['minor'])
        if response['status'] == 'ok':
            return response['data'] if 'data' in response else dict()
        raise Exception('Invalid status found in SOAP response')
    raise Exception('Invalid response')