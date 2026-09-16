def rpc_is_name_zonefile_hash(self, name, zonefile_hash, **con_info):
    if not check_name(name) and not check_subdomain(name):
        return {'error': 'invalid name', 'http_status': 400}
    if not check_string(zonefile_hash, min_length=LENGTHS['value_hash'] * 2,
        max_length=LENGTHS['value_hash'] * 2, pattern=OP_HEX_PATTERN):
        return {'error': 'invalid zone file hash', 'http_status': 400}
    was_set = None
    if check_name(name):
        db = get_db_state(self.working_dir)
        was_set = db.is_name_zonefile_hash(name, zonefile_hash)
        db.close()
    else:
        was_set = is_subdomain_zonefile_hash(name, zonefile_hash)
    return self.success_response({'result': was_set})