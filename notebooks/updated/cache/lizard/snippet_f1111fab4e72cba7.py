def basic_publish(self, msg, exchange='', routing_key='', mandatory=False,
    immediate=False, ticket=None):
    args = AMQPWriter()
    if ticket is not None:
        args.write_short(ticket)
    else:
        args.write_short(self.default_ticket)
    args.write_shortstr(exchange)
    args.write_shortstr(routing_key)
    args.write_bit(mandatory)
    args.write_bit(immediate)
    self._send_method((60, 40), args, msg)