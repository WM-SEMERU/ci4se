def unrecord(plugin_or_specs, filename):
    plugin, filename = normalize_migration(plugin_or_specs, filename)
    migration = get_migration(plugin, filename)
    if migration:
        log.info('Removing migration %s:%s', plugin, filename)
        db = get_db()
        db.eval(UNRECORD_WRAPPER, migration['_id'])
    else:
        log.error('Migration not found %s:%s', plugin, filename)