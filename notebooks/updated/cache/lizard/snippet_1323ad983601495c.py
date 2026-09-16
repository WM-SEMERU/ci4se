def do_not_run(self):
    logger.debug('[%s] do_not_run', self.name)
    try:
        self.con.get('_do_not_run')
        return True
    except HTTPClientConnectionException as exp:
        self.add_failed_check_attempt(
            'Connection error when sending do not run: %s' % str(exp))
        self.set_dead()
    except HTTPClientTimeoutException as exp:
        self.add_failed_check_attempt(
            'Connection timeout when sending do not run: %s' % str(exp))
    except HTTPClientException as exp:
        self.add_failed_check_attempt('Error when sending do not run: %s' %
            str(exp))
    return False