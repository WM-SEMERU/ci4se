def process_message(self, ch, method, properties, body):
    self.work_request = pickle.loads(body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    self.process_work_request()