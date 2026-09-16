def fileserver_update(fileserver):
    try:
        if not fileserver.servers:
            log.error(
                'No fileservers loaded, the master will not be able to serve files to minions'
                )
            raise salt.exceptions.SaltMasterError(
                'No fileserver backends available')
        fileserver.update()
    except Exception as exc:
        log.error('Exception %s occurred in file server update', exc,
            exc_info_on_loglevel=logging.DEBUG)