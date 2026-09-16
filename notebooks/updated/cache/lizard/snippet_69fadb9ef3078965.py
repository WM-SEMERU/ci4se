def send_message_batch(self, queue, messages):
    params = {}
    for i, msg in enumerate(messages):
        p_name = 'SendMessageBatchRequestEntry.%i.Id' % (i + 1)
        params[p_name] = msg[0]
        p_name = 'SendMessageBatchRequestEntry.%i.MessageBody' % (i + 1)
        params[p_name] = msg[1]
        p_name = 'SendMessageBatchRequestEntry.%i.DelaySeconds' % (i + 1)
        params[p_name] = msg[2]
    return self.get_object('SendMessageBatch', params, BatchResults, queue.
        id, verb='POST')