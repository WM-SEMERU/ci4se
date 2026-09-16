def receive_request(self, transaction):
    with transaction:
        transaction.separate_timer = self._start_separate_timer(transaction)
        self._blockLayer.receive_request(transaction)
        if transaction.block_transfer:
            self._stop_separate_timer(transaction.separate_timer)
            self._messageLayer.send_response(transaction)
            self.send_datagram(transaction.response)
            return
        self._observeLayer.receive_request(transaction)
        self._requestLayer.receive_request(transaction)
        if transaction.resource is not None and transaction.resource.changed:
            self.notify(transaction.resource)
            transaction.resource.changed = False
        elif transaction.resource is not None and transaction.resource.deleted:
            self.notify(transaction.resource)
            transaction.resource.deleted = False
        self._observeLayer.send_response(transaction)
        self._blockLayer.send_response(transaction)
        self._stop_separate_timer(transaction.separate_timer)
        self._messageLayer.send_response(transaction)
        if transaction.response is not None:
            if transaction.response.type == defines.Types['CON']:
                self._start_retransmission(transaction, transaction.response)
            self.send_datagram(transaction.response)