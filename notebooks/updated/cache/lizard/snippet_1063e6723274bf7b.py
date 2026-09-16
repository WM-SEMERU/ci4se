def blocking_navigate(self, url, timeout=DEFAULT_TIMEOUT_SECS):
    self.transport.flush(tab_key=self.tab_id)
    ret = self.Page_navigate(url=url)
    assert 'result' in ret, 'Missing return content'
    assert 'frameId' in ret['result'], "Missing 'frameId' in return content"
    assert 'loaderId' in ret['result'], "Missing 'loaderId' in return content"
    expected_id = ret['result']['frameId']
    loader_id = ret['result']['loaderId']
    try:
        self.log.debug('Waiting for frame navigated command response.')
        self.transport.recv_filtered(filter_funcs.
            check_frame_navigated_command(expected_id), tab_key=self.tab_id,
            timeout=timeout)
        self.log.debug('Waiting for frameStartedLoading response.')
        self.transport.recv_filtered(filter_funcs.check_frame_load_command(
            'Page.frameStartedLoading'), tab_key=self.tab_id, timeout=timeout)
        self.log.debug('Waiting for frameStoppedLoading response.')
        self.transport.recv_filtered(filter_funcs.check_frame_load_command(
            'Page.frameStoppedLoading'), tab_key=self.tab_id, timeout=timeout)
        self.log.debug('Waiting for responseReceived response.')
        resp = self.transport.recv_filtered(filter_funcs.
            network_response_recieved_for_url(url=None, expected_id=
            expected_id), tab_key=self.tab_id, timeout=timeout)
        if resp is None:
            raise ChromeNavigateTimedOut('Blocking navigate timed out!')
        return resp['params']
    except ChromeResponseNotReceived:
        self.log.warning(
            'Failed to receive expected response to navigate command. Checking if response is a binary object.'
            )
        resp = self.transport.recv_filtered(keycheck=filter_funcs.
            check_frame_loader_command(method_name=
            'Network.responseReceived', loader_id=loader_id), tab_key=self.
            tab_id, timeout=timeout)
        return resp['params']