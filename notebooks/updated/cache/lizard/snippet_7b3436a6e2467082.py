def read_queue(self):
    queue = AmazonSQS().create_queue(settings.RESTCLIENTS_AMAZON_QUEUE)
    queue.set_message_class(RawMessage)
    message = queue.read()
    if message is None:
        return
    body = message.get_body()
    queue.delete_message(message)
    return body