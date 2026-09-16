def direct_command_short(self, command):
    self.logger.info('direct_command_short: Command %s', command)
    command_url = self.hub_url + '/3?' + command + '=I=0'
    return self.post_direct_command(command_url)