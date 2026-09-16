def digital_channel_cable(self, opt1='?', opt2=0):
    if opt1 == '?':
        parameter = '?'
    elif self.command['digital_channel_cable_minor'] == '':
        parameter = str(opt1).rjust(4, '0')
    else:
        self._send_command('digital_channel_cable_minor', str(opt1).rjust(3,
            '0'))
        parameter = str(opt2).rjust(3, '0')
    return self._send_command('digital_channel_cable_major', parameter)