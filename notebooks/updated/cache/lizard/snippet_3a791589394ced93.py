def create_queue(self, queue_name, visibility_timeout=None, callback=None):
    params = {'QueueName': queue_name}
    if visibility_timeout:
        params['DefaultVisibilityTimeout'] = '%d' % (visibility_timeout,)
    return self.get_object('CreateQueue', params, botornado.sqs.queue.
        AsyncQueue, callback=callback)