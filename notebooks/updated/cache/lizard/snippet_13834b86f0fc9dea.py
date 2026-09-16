def _wrap_result(self, response):
    if isinstance(response, int):
        response = self._wrap_response(response)
    return HandlerResult(status=HandlerStatus.RETURN, message_out=self.
        _response_proto(**response), message_type=self._response_type)