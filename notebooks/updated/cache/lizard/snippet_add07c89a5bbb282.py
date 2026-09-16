def cmd_join(self, connection, sender, target, payload):
    if payload:
        connection.join(payload)
    else:
        raise ValueError('No channel given')