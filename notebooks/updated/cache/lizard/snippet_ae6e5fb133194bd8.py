def get_status(self):
    try:
        c = self._oc_command(['status'])
        o = run_cmd(c, return_output=True)
        for line in o.split('\n'):
            logger.debug(line)
        return o
    except subprocess.CalledProcessError as ex:
        raise ConuException('Cannot obtain OpenShift cluster status: %s' % ex)