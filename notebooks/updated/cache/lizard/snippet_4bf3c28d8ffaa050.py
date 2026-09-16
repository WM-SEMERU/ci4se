def submit(self, func, *args, **kwargs):
    self.op_sequence += 1
    self.sqs.send_message(QueueUrl=self.map_queue, MessageBody=utils.dumps(
        {'args': args, 'kwargs': kwargs}), MessageAttributes={'sequence_id':
        {'StringValue': str(self.op_sequence), 'DataType': 'Number'}, 'op':
        {'StringValue': named(func), 'DataType': 'String'}, 'ser': {
        'StringValue': 'json', 'DataType': 'String'}})
    self.futures[self.op_sequence] = f = SQSFuture(self.op_sequence)
    return f