def get_entity_info(pdb_id):
    out = get_info(pdb_id, url_root=
        'http://www.rcsb.org/pdb/rest/getEntityInfo?structureId=')
    out = to_dict(out)
    return remove_at_sign(out['entityInfo']['PDB'])