def start_fileoutput(self):
    path = os.path.dirname(self.filename)
    try:
        if path and not os.path.isdir(path):
            os.makedirs(path)
        self.fd = self.create_fd()
        self.close_fd = True
    except IOError:
        msg = sys.exc_info()[1]
        log.warn(LOG_CHECK,
            'Could not open file %r for writing: %s\nDisabling log output of %s'
            , self.filename, msg, self)
        self.fd = dummy.Dummy()
        self.is_active = False
    self.filename = None