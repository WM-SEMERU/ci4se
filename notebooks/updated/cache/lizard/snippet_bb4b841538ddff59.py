def send(self, request, blocking=True):
    future = Future()
    if self.connecting():
        return future.failure(Errors.NodeNotReadyError(str(self)))
    elif not self.connected():
        return future.failure(Errors.KafkaConnectionError(str(self)))
    elif not self.can_send_more():
        return future.failure(Errors.TooManyInFlightRequests(str(self)))
    return self._send(request, blocking=blocking)