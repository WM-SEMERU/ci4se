def verification_cancel(self, verification_id, reason=None):
    data = {'cancel': True, 'cancel_reason': reason}
    response = self._put(url.verifications_id.format(id=verification_id),
        body=data)
    self._check_response(response, 202)