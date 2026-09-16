def _handle_command(self, connection, sender, target, command, payload):
    try:
        handler = getattr(self, 'cmd_{0}'.format(command))
    except AttributeError:
        self.safe_send(connection, target, 'Unknown command: %s', command)
    else:
        try:
            logging.info('! Handling command: %s', command)
            handler(connection, sender, target, payload)
        except Exception as ex:
            logging.exception('Error calling command handler: %s', ex)