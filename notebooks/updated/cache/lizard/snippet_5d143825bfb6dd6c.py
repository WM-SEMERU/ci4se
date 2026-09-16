def get_ugali_dir():
    dirname = os.getenv('UGALIDIR')
    if not dirname:
        dirname = os.path.join(os.getenv('HOME'), '.ugali')
    if not os.path.exists(dirname):
        from ugali.utils.logger import logger
        msg = 'Creating UGALIDIR:\n%s' % dirname
        logger.warning(msg)
    return mkdir(dirname)