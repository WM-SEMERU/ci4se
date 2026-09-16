def handle_database(self):
    if self.args.initdb or self.args.upgradedb:
        db = DbAdmin(self.dir, None, self.args, self.external)
        status = db.check()
        log.debug('OMERO database upgrade status: %s', status)
    else:
        log.warn('OMERO database check disabled')
        return DB_INIT_NEEDED
    if status == DB_INIT_NEEDED:
        if self.args.initdb:
            log.debug('Initialising OMERO database')
            db.init()
        else:
            log.error('OMERO database not found')
            raise Stop(DB_INIT_NEEDED,
                'Install/Upgrade failed: OMERO database not found')
    elif status == DB_UPGRADE_NEEDED:
        log.warn('OMERO database exists but is out of date')
        if self.args.upgradedb:
            log.debug('Upgrading OMERO database')
            db.upgrade()
        else:
            raise Stop(DB_UPGRADE_NEEDED,
                'Pass --managedb or upgrade your OMERO database manually')
    else:
        assert status == DB_UPTODATE
    return status