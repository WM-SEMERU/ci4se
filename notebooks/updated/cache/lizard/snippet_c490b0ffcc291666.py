def set_cons3rt_role_name(self):
    log = logging.getLogger(self.cls_logger + '.set_cons3rt_role_name')
    try:
        self.cons3rt_role_name = os.environ['CONS3RT_ROLE_NAME']
    except KeyError:
        log.warn(
            'CONS3RT_ROLE_NAME is not set, attempting to determine it from deployment properties...'
            )
        if platform.system() == 'Linux':
            log.info('Attempting to determine CONS3RT_ROLE_NAME on Linux...')
            try:
                self.determine_cons3rt_role_name_linux()
            except DeploymentError:
                raise
        else:
            log.warn('Unable to determine CONS3RT_ROLE_NAME on this System')
    else:
        log.info('Found environment variable CONS3RT_ROLE_NAME: {r}'.format
            (r=self.cons3rt_role_name))
        return