async def handle_client_message(self, client_addr, message):
    if (message.__class__ != ClientHello and client_addr not in self.
        _registered_clients):
        await ZMQUtils.send_with_addr(self._client_socket, client_addr,
            Unknown())
        return
    message_handlers = {ClientHello: self.handle_client_hello, ClientNewJob:
        self.handle_client_new_job, ClientKillJob: self.
        handle_client_kill_job, ClientGetQueue: self.
        handle_client_get_queue, Ping: self.handle_client_ping}
    try:
        func = message_handlers[message.__class__]
    except:
        raise TypeError('Unknown message type %s' % message.__class__)
    self._create_safe_task(func(client_addr, message))