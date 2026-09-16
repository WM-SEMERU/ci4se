def _basic_return(self, args, msg):
    reply_code = args.read_short()
    reply_text = args.read_shortstr()
    exchange = args.read_shortstr()
    routing_key = args.read_shortstr()
    self.returned_messages.put((reply_code, reply_text, exchange,
        routing_key, msg))