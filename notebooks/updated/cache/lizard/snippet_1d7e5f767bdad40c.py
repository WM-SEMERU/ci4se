def change_autocommit_mode(self, switch):
    parsed_switch = switch.strip().lower()
    if not parsed_switch in ['true', 'false']:
        self.send_response(self.iopub_socket, 'stream', {'name': 'stderr',
            'text': """autocommit must be true or false.

"""})
    switch_bool = parsed_switch == 'true'
    committed = self.switch_autocommit(switch_bool)
    message = ('committed current transaction & ' if committed else '' +
        'switched autocommit mode to ' + str(self._autocommit))
    self.send_response(self.iopub_socket, 'stream', {'name': 'stderr',
        'text': message})