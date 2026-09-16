def GET_blockchain_ops(self, path_info, blockchain_name, blockheight):
    try:
        blockheight = int(blockheight)
        assert check_block(blockheight)
    except:
        return self._reply_json({'error': 'Invalid block'}, status_code=400)
    if blockchain_name != 'bitcoin':
        return self._reply_json({'error': 'Unsupported blockchain'},
            status_code=404)
    blockstackd_url = get_blockstackd_url()
    nameops = blockstackd_client.get_blockstack_transactions_at(int(
        blockheight), hostport=blockstackd_url)
    if json_is_error(nameops):
        status_code = nameops.get('http_status', 502)
        return self._reply_json({'error': nameops['error']}, status_code=
            status_code)
    self._reply_json(nameops)
    return