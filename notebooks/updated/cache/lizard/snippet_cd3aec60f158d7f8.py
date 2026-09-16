def send_and_wait(self, message, params=None, timeout=10, raises=False):
    job_id = self.send(message, params)
    resp = self.wait_event(job_id, timeout, raises=raises)
    return (None, None) if resp is None else resp