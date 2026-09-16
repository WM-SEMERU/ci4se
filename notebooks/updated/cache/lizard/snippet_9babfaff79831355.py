def close(self):
    scoop.logger.debug('Closing broker on host {0}.'.format(self.hostname))
    try:
        self.shell.terminate()
    except OSError:
        pass
    sys.stdout.write(self.shell.stdout.read().decode('utf-8'))
    sys.stdout.flush()
    sys.stderr.write(self.shell.stderr.read().decode('utf-8'))
    sys.stderr.flush()