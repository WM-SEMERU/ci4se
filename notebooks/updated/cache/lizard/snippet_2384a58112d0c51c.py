def setup_auditlog_catalog(portal):
    logger.info('*** Setup Audit Log Catalog ***')
    catalog_id = auditlog_catalog.CATALOG_AUDITLOG
    catalog = api.get_tool(catalog_id)
    for name, meta_type in auditlog_catalog._indexes.iteritems():
        indexes = catalog.indexes()
        if name in indexes:
            logger.info("*** Index '%s' already in Catalog [SKIP]" % name)
            continue
        logger.info("*** Adding Index '%s' for field '%s' to catalog ..." %
            (meta_type, name))
        catalog.addIndex(name, meta_type)
        if meta_type == 'TextIndexNG3':
            index = catalog._catalog.getIndex(name)
            index.index.default_encoding = 'utf-8'
            index.index.query_parser = 'txng.parsers.en'
            index.index.autoexpand = 'always'
            index.index.autoexpand_limit = 3
        logger.info("*** Added Index '%s' for field '%s' to catalog [DONE]" %
            (meta_type, name))
    at = api.get_tool('archetype_tool')
    pt = api.get_tool('portal_types')
    for portal_type in pt.listContentTypes():
        catalogs = at.getCatalogsByType(portal_type)
        if catalog not in catalogs:
            new_catalogs = map(lambda c: c.getId(), catalogs) + [catalog_id]
            at.setCatalogsByType(portal_type, new_catalogs)
            logger.info("*** Adding catalog '{}' for '{}'".format(
                catalog_id, portal_type))