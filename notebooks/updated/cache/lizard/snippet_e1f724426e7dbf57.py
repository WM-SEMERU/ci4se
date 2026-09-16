def migrate(connection, dsn):
    all_migrations = _get_all_migrations()
    logger.debug('Collected migrations: {}'.format(all_migrations))
    for version, modname in all_migrations:
        if _is_missed(connection, version) and version <= SCHEMA_VERSION:
            logger.info(
                'Missed migration: {} migration is missed. Migrating...'.
                format(version))
            module = __import__(modname, fromlist='dummy')
            trans = connection.begin()
            try:
                module.Migration().migrate(connection)
                _update_version(connection, version)
                trans.commit()
            except:
                trans.rollback()
                logger.error("Failed to migrate '{}'  on {} ".format(
                    version, dsn))
                raise