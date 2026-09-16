def GET_account_record(self, path_info, account_addr, token_type):
    if not check_account_address(account_addr):
        return self._reply_json({'error': 'Invalid address'}, status_code=400)
    if not check_token_type(token_type):
        return self._reply_json({'error': 'Invalid token type'},
            status_code=400)
    blockstackd_url = get_blockstackd_url()
    res = blockstackd_client.get_account_record(account_addr, token_type,
        hostport=blockstackd_url)
    if json_is_error(res):
        log.error('Failed to get account state for {} {}: {}'.format(
            account_addr, token_type, res['error']))
        return self._reply_json({'error':
            'Failed to get account record for {} {}: {}'.format(token_type,
            account_addr, res['error'])}, status_code=res.get('http_status',
            500))
    self._reply_json(res)
    return