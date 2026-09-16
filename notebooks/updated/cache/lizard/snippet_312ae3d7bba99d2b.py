def log_message(self, fmt, *fmt_args):
    msg = self.my_address_string() + ' - - ' + fmt % fmt_args
    my_log_message(args, syslog.LOG_INFO, msg)