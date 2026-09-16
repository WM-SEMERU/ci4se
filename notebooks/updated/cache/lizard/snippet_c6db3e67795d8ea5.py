def get_DID_name(self, did):
    did = str(did)
    did_info = None
    try:
        did_info = parse_DID(did)
        assert did_info['name_type'] == 'name'
    except Exception as e:
        if BLOCKSTACK_DEBUG:
            log.exception(e)
        raise ValueError('Invalid DID: {}'.format(did))
    cur = self.db.cursor()
    historic_name_info = namedb_get_historic_names_by_address(cur, did_info
        ['address'], offset=did_info['index'], count=1)
    if historic_name_info is None:
        return None
    name = historic_name_info[0]['name']
    block_height = historic_name_info[0]['block_id']
    vtxindex = historic_name_info[0]['vtxindex']
    log.debug('DID {} refers to {}-{}-{}'.format(did, name, block_height,
        vtxindex))
    name_rec = self.get_name(name, include_history=True, include_expired=True)
    if name_rec is None:
        return None
    name_rec_latest = None
    found = False
    for height in sorted(name_rec['history'].keys()):
        if found:
            break
        if height < block_height:
            continue
        for state in name_rec['history'][height]:
            if height == block_height and state['vtxindex'] < vtxindex:
                continue
            if state['op'] == NAME_PREORDER:
                found = True
                break
            if state['revoked']:
                log.debug(
                    'DID {} refers to {}-{}-{}, which is revoked at {}-{}'.
                    format(did, name, block_height, vtxindex, height, state
                    ['vtxindex']))
                return None
            name_rec_latest = state
    return name_rec_latest