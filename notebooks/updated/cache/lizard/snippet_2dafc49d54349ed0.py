def _url_for_queue(self, conn, name):
    res = conn.get_queue_url(QueueName=name)
    return res['QueueUrl']