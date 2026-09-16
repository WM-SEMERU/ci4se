def dispatch_command(self, command, params=None):
    try:
        if command in self.handlers:
            self.handlers[command](**params)
        else:
            logging.warning('Unsupported command: %s: %s', command, params)
    except Exception as e:
        logging.warning('Error during command execution', exc_info=sys.
            exc_info())
        raise e