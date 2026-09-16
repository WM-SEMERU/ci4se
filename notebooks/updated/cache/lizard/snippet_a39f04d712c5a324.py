def input(self, opt):
    for key in self.command['input']:
        if key == opt or self.command['input'][key]['name'] == opt:
            return self._send_command(['input', key, 'command'])
    return False