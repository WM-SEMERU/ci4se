def move(source, destination):
    logger.info('Move: %s -> %s' % (source, destination))
    try:
        __create_destdir(destination)
        shutil.move(source, destination)
        return True
    except Exception:
        logger.exception('Failed to Move: %s -> %s' % (source, destination))
        return False