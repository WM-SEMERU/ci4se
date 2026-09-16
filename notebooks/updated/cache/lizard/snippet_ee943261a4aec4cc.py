def receive_response(self, transaction):
    host, port = transaction.response.source
    key_token = hash(str(host) + str(port) + str(transaction.response.token))
    if (key_token in self._relations and transaction.response.type ==
        defines.Types['CON']):
        transaction.notification = True
    return transaction