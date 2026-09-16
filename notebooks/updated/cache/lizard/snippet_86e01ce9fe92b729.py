def get_subdomain_DID_record(self, did):
    try:
        did_info = parse_DID(did)
        assert did_info['name_type'] == 'subdomain'
    except Exception as e:
        if BLOCKSTACK_DEBUG:
            log.exception(e)
        return {'error': 'Invalid DID', 'http_status': 400}
    subrec = get_DID_subdomain(did, check_pending=True)
    if subrec is None:
        return {'error': 'Failed to load subdomain from {}'.format(did),
            'http_status': 404}
    return {'record': subrec.to_json()}