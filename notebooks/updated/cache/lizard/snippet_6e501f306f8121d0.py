def complex_request(self, request, wait_for_first_response=True):
    receiver = self._prepare_response_receiver(request, receiver_class=
        CommandResponseReceiver)
    self._send_complex_request(request)
    responses = []
    if wait_for_first_response:
        responses = receiver.wait_for_responses()
    return responses