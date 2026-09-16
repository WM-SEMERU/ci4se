def clean_project(self, app_name=None, delete_all=False):
    if not app_name and not delete_all:
        ConuException(
            'You need to specify either app_name or set delete_all=True')
    if delete_all:
        args = ['--all']
        logger.info('Deleting all objects in current project')
    else:
        args = '-l app=%s' % app_name
        logger.info('Deleting all objects with label app=%s', app_name)
    try:
        o = run_cmd(self._oc_command(['delete', 'all', args]),
            return_output=True)
        o_lines = o.split('\n')
        for line in o_lines:
            logger.info(line)
    except subprocess.CalledProcessError as ex:
        raise ConuException('Cleanup failed because of exception: %s' % ex)