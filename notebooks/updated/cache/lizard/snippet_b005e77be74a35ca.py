def cancel_queue(self):
    q = list(self.queue)
    self.queue = []
    log.debug('Canceling requests: {}'.format(q))
    for req in q:
        req.response = APIServerNotRunningErrorResponse()
    for req in q:
        req.signal()