def format_request(self):
    fmt = (
        '{now} {status} {requestline} ({client_address}) {response_length} {delta}ms'
        )
    requestline = getattr(self, 'requestline')
    if requestline:
        requestline = ' '.join(requestline.split(' ')[:-1])
    else:
        requestline = '???'
    if self.time_finish:
        delta = '%.2f' % ((self.time_finish - self.time_start) * 1000)
    else:
        delta = '-'
    data = dict(now=datetime.datetime.now().replace(microsecond=0),
        response_length=self.response_length or '-', client_address=self.
        client_address[0] if isinstance(self.client_address, tuple) else
        self.client_address, status=str(self._get_status_int()),
        requestline=requestline, delta=delta)
    return fmt.format(**data)