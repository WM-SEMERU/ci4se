def set_keyspace_async(self, keyspace, callback):
    while True:
        with self.lock:
            if self.in_flight < self.max_request_id:
                self.in_flight += 1
                break
        time.sleep(0.001)
    if not keyspace or keyspace == self.keyspace:
        callback(self, None)
        return
    query = QueryMessage(query='USE "%s"' % (keyspace,), consistency_level=
        ConsistencyLevel.ONE)

    def process_result(result):
        if isinstance(result, ResultMessage):
            self.keyspace = keyspace
            callback(self, None)
        elif isinstance(result, InvalidRequestException):
            callback(self, result.to_exception())
        else:
            callback(self, self.defunct(ConnectionException(
                'Problem while setting keyspace: %r' % (result,), self.
                endpoint)))
    request_id = self.get_request_id()
    self.send_msg(query, request_id, process_result)