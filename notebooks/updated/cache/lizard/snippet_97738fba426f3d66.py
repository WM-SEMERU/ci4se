def send_message(self, message):
    for handler in self.users:
        logging.info('Handler: ' + str(handler))
        handler.write_message(message)