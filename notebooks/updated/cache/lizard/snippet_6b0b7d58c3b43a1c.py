def atlasdb_queue_zonefiles(con, db, start_block, zonefile_dir, recover=
    False, validate=True, end_block=None):
    total = 0
    if end_block is None:
        end_block = db.lastblock + 1
    ret = []
    for block_height in range(start_block, end_block, 1):
        zonefile_info = db.get_atlas_zonefile_info_at(block_height)
        for name_txid_zfhash in zonefile_info:
            name = str(name_txid_zfhash['name'])
            zfhash = str(name_txid_zfhash['value_hash'])
            txid = str(name_txid_zfhash['txid'])
            tried_storage = 0
            present = is_zonefile_cached(zfhash, zonefile_dir, validate=
                validate)
            zfinfo = atlasdb_get_zonefile(zfhash, con=con)
            if zfinfo is not None:
                tried_storage = zfinfo['tried_storage']
            if recover and present:
                log.debug(
                    'Recover: assume that {} is absent so we will reprocess it'
                    .format(zfhash))
                present = False
            log.debug('Add %s %s %s at %s (present: %s, tried_storage: %s)' %
                (name, zfhash, txid, block_height, present, tried_storage))
            atlasdb_add_zonefile_info(name, zfhash, txid, present,
                tried_storage, block_height, con=con)
            total += 1
            ret.append({'name': name, 'zonefile_hash': zfhash, 'txid': txid,
                'block_height': block_height, 'present': present,
                'tried_storage': tried_storage})
    log.debug('Queued %s zonefiles from %s-%s' % (total, start_block, db.
        lastblock))
    return ret