def log_message(self, msg, *args):
    if args:
        msg = msg % args
    self.logger.info(msg)