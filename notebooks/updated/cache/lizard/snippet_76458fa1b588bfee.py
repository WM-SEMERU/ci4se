def add_atlas_zonefile_data(zonefile_text, zonefile_dir, fsync=True):
    rc = store_atlas_zonefile_data(zonefile_text, zonefile_dir, fsync=fsync)
    if not rc:
        zonefile_hash = get_zonefile_data_hash(zonefile_text)
        log.error('Failed to save zonefile {}'.format(zonefile_hash))
        rc = False
    return rc