def _get_all_volumes_paths(conn):
    volumes = [vol for l in [obj.listAllVolumes() for obj in conn.
        listAllStoragePools()] for vol in l]
    return {vol.path(): [path.text for path in ElementTree.fromstring(vol.
        XMLDesc()).findall('.//backingStore/path')] for vol in volumes if
        _is_valid_volume(vol)}