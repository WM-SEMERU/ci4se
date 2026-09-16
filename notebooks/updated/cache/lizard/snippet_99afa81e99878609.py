def external_account_cmd_by_name(self, command_name):
    return self._cmd(command_name, data=self.name, api_version=16)