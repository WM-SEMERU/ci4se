def GET_zonefile(self, path_info, zonefile_hash):
    if not check_string(zonefile_hash, pattern=OP_ZONEFILE_HASH_PATTERN):
        return self._reply_json({'error': 'Invalid zone file hash'},
            status_code=400)
    blockstackd_url = get_blockstackd_url()
    resp = blockstackd_client.get_zonefiles(blockstackd_url, [str(
        zonefile_hash)])
    if json_is_error(resp):
        log.error('Failed to get {}: {}'.format(zonefile_hash, resp['error']))
        return self._reply_json({'error': resp['error']}, status_code=resp.
            get('http_status', 502))
    if str(zonefile_hash) not in resp['zonefiles']:
        return self._reply_json({'error':
            'Blockstack node does not have this zonefile.  Try again later.'
            }, status_code=404)
    self._send_headers(status_code=200, content_type='application/octet-stream'
        )
    self.wfile.write(resp['zonefiles'][str(zonefile_hash)])
    return