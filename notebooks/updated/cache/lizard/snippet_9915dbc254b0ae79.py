def is_running(self):
    cmd = ['machinectl', '--no-pager', 'status', self.name]
    try:
        subprocess.check_call(cmd)
        return True
    except subprocess.CalledProcessError as ex:
        logger.info('nspawn container %s is not running probably: %s', self
            .name, ex.output)
        return False