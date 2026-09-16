def get_name_DID_record(self, did):
    try:
        did_info = parse_DID(did)
        assert did_info['name_type'] == 'name'
    except Exception as e:
        if BLOCKSTACK_DEBUG:
            log.exception(e)
        return {'error': 'Invalid DID', 'http_status': 400}
    db = get_db_state(self.working_dir)
    rec = db.get_DID_name(did)
    if rec is None:
        db.close()
        return {'error': 'Failed to resolve DID to a non-revoked name',
            'http_status': 404}
    name_record = self.load_name_info(db, rec)
    db.close()
    if name_record is None:
        return {'error': 'DID does not resolve to an existing name',
            'http_status': 404}
    return {'record': name_record}