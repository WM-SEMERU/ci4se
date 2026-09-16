def send(self, message):
    for event in message.events:
        self.events.append(event)
    reply = riemann_client.riemann_pb2.Msg()
    reply.ok = True
    return reply