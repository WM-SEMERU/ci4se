def synchronous_command(self, command, tab_key, **params):
    self.log.debug('Synchronous_command to tab %s (%s):', tab_key, self.
        _get_cr_tab_meta_for_key(tab_key))
    self.log.debug("\tcommand: '%s'", command)
    self.log.debug("\tparams:  '%s'", params)
    self.log.debug("\ttab_key:  '%s'", tab_key)
    send_id = self.send(command=command, tab_key=tab_key, params=params)
    resp = self.recv(message_id=send_id, tab_key=tab_key)
    self.log.debug("\tResponse: '%s'", str(resp).encode('ascii', 'ignore').
        decode('ascii'))
    return resp