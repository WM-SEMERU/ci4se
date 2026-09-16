def _getresult(self, captcha_id, timeout=None):
    timeout = timeout
    if not timeout:
        timeout = self.waittime
    poll_interval = 8
    start = time.time()
    for x in range(int(timeout / poll_interval) + 1):
        self.log.info(
            'Sleeping %s seconds (poll %s of %s, elapsed %0.2fs of %0.2f).',
            poll_interval, x, int(timeout / poll_interval) + 1, time.time() -
            start, timeout)
        time.sleep(poll_interval)
        try:
            resp = self.doGet('result', {'action': 'get', 'key': self.
                api_key, 'json': True, 'id': captcha_id})
            self.log.info('Call returned success!')
            return resp
        except exc.CaptchaNotReady:
            self.log.info('Captcha not ready. Waiting longer.')
    raise exc.CaptchaSolverFailure(
        'Solving captcha timed out after %s seconds!' % (time.time() - start,))