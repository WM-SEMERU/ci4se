def quit(self):
    self.script.LOG.warn('Abort due to user choice!')
    sys.exit(self.QUIT_RC)