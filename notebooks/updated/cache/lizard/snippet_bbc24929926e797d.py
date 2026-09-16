def cli(self, command):
    if not self.connected:
        raise pyPluribus.exceptions.ConnectionError(
            'Not connected to the deivce.')
    cli_output = ''
    ssh_session = self._connection.get_transport().open_session()
    ssh_session.settimeout(self._timeout)
    ssh_session.exec_command(command)
    ssh_output = ''
    err_output = ''
    ssh_output_makefile = ssh_session.makefile()
    ssh_error_makefile = ssh_session.makefile_stderr()
    for byte_output in ssh_output_makefile:
        ssh_output += byte_output
    for byte_error in ssh_error_makefile:
        err_output += byte_error
    if not ssh_output:
        if err_output:
            raise pyPluribus.exceptions.CommandExecutionError(err_output)
    cli_output = '\n'.join(ssh_output.split(self._ssh_banner)[-1].
        splitlines()[1:])
    if cli_output == 'Please enter username and password:':
        self.open()
        return self.cli(command)
    return cli_output