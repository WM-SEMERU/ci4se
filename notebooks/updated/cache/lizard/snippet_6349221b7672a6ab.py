def stop(self):
    logger.debug('reading %s' % (self.pidfile,))
    try:
        with open(self.pidfile, 'r') as fd:
            pid = int(fd.read().strip())
    except IOError:
        logger.exception('reading %s' % (self.pidfile,))
        pid = None
    if not pid:
        message = 'pidfile %s does not exist. Daemon not running?\n'
        sys.stderr.write(message % self.pidfile)
        return
    if os.name == 'nt':
        subprocess.call(['taskkill', '/f', '/t', '/pid', str(pid)])
        if os.path.exists(self.pidfile):
            os.remove(self.pidfile)
    else:
        try:
            os.kill(pid, SIGTERM)
        except OSError as err:
            err = str(err)
            if err.find('No such process') > 0:
                if os.path.exists(self.pidfile):
                    os.remove(self.pidfile)
            else:
                raise