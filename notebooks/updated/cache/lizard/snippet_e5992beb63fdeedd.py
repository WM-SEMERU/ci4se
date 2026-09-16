def rpc_get_zonefiles(self, zonefile_hashes, **con_info):
    conf = get_blockstack_opts()
    if not is_atlas_enabled(conf):
        return {'error': 'No data', 'http_status': 400}
    if 'zonefiles' not in conf:
        return {'error':
            'No zonefiles directory (likely a configuration bug)',
            'http_status': 404}
    if type(zonefile_hashes) != list:
        log.error('Not a zonefile hash list')
        return {'error': 'Invalid zonefile hashes', 'http_status': 400}
    if len(zonefile_hashes) > 100:
        log.error('Too many requests (%s)' % len(zonefile_hashes))
        return {'error': 'Too many requests (no more than 100 allowed)',
            'http_status': 400}
    for zfh in zonefile_hashes:
        if not check_string(zfh, min_length=LENGTHS['value_hash'] * 2,
            max_length=LENGTHS['value_hash'] * 2, pattern=OP_HEX_PATTERN):
            return {'error': 'Invalid zone file hash', 'http_status': 400}
    ret = {}
    for zonefile_hash in zonefile_hashes:
        zonefile_data = self.get_zonefile_data(zonefile_hash, conf['zonefiles']
            )
        if zonefile_data is None:
            continue
        else:
            ret[zonefile_hash] = base64.b64encode(zonefile_data)
    log.debug('Serve back %s zonefiles' % len(ret.keys()))
    return self.success_response({'zonefiles': ret})