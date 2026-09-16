def GET_did(self, path_info, did):
    try:
        did_info = parse_DID(did)
        assert did_info['name_type'] in ('name', 'subdomain')
    except Exception as e:
        if BLOCKSTACK_DEBUG:
            log.exception(e)
        return self._reply_json({'error': 'Invalid DID'}, status_code=400)
    blockstackd_url = get_blockstackd_url()
    resp = blockstackd_client.resolve_DID(did, hostport=blockstackd_url)
    if json_is_error(resp):
        return self._reply_json({'error': resp['error']}, status_code=404)
    return self._reply_json({'public_key': resp['public_key'], 'document':
        resp['document']})