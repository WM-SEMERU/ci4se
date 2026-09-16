def enqueue(self, message, *, delay=None):
    queue_name = message.queue_name
    message = message.copy(options={'redis_message_id': str(uuid4())})
    if delay is not None:
        queue_name = dq_name(queue_name)
        message_eta = current_millis() + delay
        message = message.copy(queue_name=queue_name, options={'eta':
            message_eta})
    self.logger.debug('Enqueueing message %r on queue %r.', message.
        message_id, queue_name)
    self.emit_before('enqueue', message, delay)
    self.do_enqueue(queue_name, message.options['redis_message_id'],
        message.encode())
    self.emit_after('enqueue', message, delay)
    return message