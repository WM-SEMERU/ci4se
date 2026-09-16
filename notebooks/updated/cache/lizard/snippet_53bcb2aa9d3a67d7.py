def _map_content_types(archetype_tool, catalogs_definition):
    ct_map = {}
    to_reindex = []
    map_types = archetype_tool.catalog_map
    for catalog_id in catalogs_definition.keys():
        catalog_info = catalogs_definition.get(catalog_id, {})
        types = catalog_info.get('types', [])
        for t in types:
            tmp_l = ct_map.get(t, [])
            tmp_l.append(catalog_id)
            ct_map[t] = tmp_l
    for t in ct_map.keys():
        catalogs_list = ct_map[t]
        perv_catalogs_list = archetype_tool.catalog_map.get(t, [])
        set1 = set(catalogs_list)
        set2 = set(perv_catalogs_list)
        if set1 != set2:
            archetype_tool.setCatalogsByType(t, catalogs_list)
            to_reindex = to_reindex + list(set1 - set2) + list(set2 - set1)
    return to_reindex