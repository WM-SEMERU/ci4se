def _setup_catalog(portal, catalog_id, catalog_definition):
    reindex = False
    catalog = getToolByName(portal, catalog_id, None)
    if catalog is None:
        logger.warning('Could not find the %s tool.' % catalog_id)
        return False
    indexes_ids = catalog_definition.get('indexes', {}).keys()
    for idx in indexes_ids:
        indexed = _addIndex(catalog, idx, catalog_definition['indexes'][idx])
        reindex = True if indexed else reindex
    in_catalog_idxs = catalog.indexes()
    to_remove = list(set(in_catalog_idxs) - set(indexes_ids))
    for idx in to_remove:
        desindexed = _delIndex(catalog, idx)
        reindex = True if desindexed else reindex
    columns_ids = catalog_definition.get('columns', [])
    for col in columns_ids:
        created = _addColumn(catalog, col)
        reindex = True if created else reindex
    in_catalog_cols = catalog.schema()
    to_remove = list(set(in_catalog_cols) - set(columns_ids))
    for col in to_remove:
        desindexed = _delColumn(catalog, col)
        reindex = True if desindexed else reindex
    return reindex