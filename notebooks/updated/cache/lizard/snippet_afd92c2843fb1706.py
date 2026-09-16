def log_message(self, format, *args):
    sys.stderr.write('%s - - [%s] %s\n' % (self.address_string(), self.
        log_date_time_string(), format % args))