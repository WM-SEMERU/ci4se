def create_channel(self, queue_name):
    channel = self.connection.channel()
    channel.queue_declare(queue=queue_name, durable=True)
    return channel