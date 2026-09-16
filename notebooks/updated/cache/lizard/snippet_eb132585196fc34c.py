def _basic_cancel_notify(self, args):
    consumer_tag = args.read_shortstr()
    callback = self._on_cancel(consumer_tag)
    if callback:
        callback(consumer_tag)
    else:
        raise ConsumerCancelled(consumer_tag, (60, 30))