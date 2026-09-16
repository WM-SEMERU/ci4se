def finish(self):
    log.info('Client disconnected: %s', self.client_ident())
    response = ':%s QUIT :EOF from client' % self.client_ident()
    for channel in self.channels.values():
        if self in channel.clients:
            for client in channel.clients:
                client.send_queue.append(response)
            channel.clients.remove(self)
    if self.nick:
        self.server.clients.pop(self.nick)
    log.info('Connection finished: %s', self.client_ident())