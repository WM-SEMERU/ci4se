def upgrade_db(conn, pkg_name='openquake.server.db.schema.upgrades',
    skip_versions=()):
    upgrader = UpgradeManager.instance(conn, pkg_name)
    t0 = time.time()
    try:
        versions_applied = upgrader.upgrade(conn, skip_versions)
    except:
        conn.rollback()
        raise
    else:
        conn.commit()
    dt = time.time() - t0
    logging.info('Upgrade completed in %s seconds', dt)
    return versions_applied