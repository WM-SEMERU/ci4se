def db_exists():
    logger.info('Checking to see if %s already exists', repr(DB['NAME']))
    try:
        psql('', stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return False
    return True