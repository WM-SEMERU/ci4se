def __copyfile(source, destination):
    logger.info('copyfile: %s -> %s' % (source, destination))
    try:
        __create_destdir(destination)
        shutil.copy(source, destination)
        return True
    except Exception as e:
        logger.error('copyfile: %s -> %s failed! Error: %s', source,
            destination, e)
        return False