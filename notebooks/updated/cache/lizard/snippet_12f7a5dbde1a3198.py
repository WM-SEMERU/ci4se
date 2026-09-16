def op_cmd(self, command, req_format='text', xpath_expr=''):
    if not command:
        raise InvalidCommandError("Parameter 'command' cannot be empty")
    if req_format.lower() == 'xml' or xpath_expr:
        command = command.strip() + ' | display xml'
    command = command.strip() + ' | no-more\n'
    out = ''
    if self.username == 'root':
        self._shell.send(command)
        time.sleep(3)
        while self._shell.recv_ready():
            out += self._shell.recv(999999)
            time.sleep(0.75)
        out = '\n'.join(out.split('\n')[1:-2])
    else:
        stdin, stdout, stderr = self._session.exec_command(command=command,
            timeout=float(self.session_timeout))
        stdin.close()
        while not stdout.channel.exit_status_ready():
            out += stdout.read()
        stdout.close()
        while not stderr.channel.exit_status_ready():
            out += stderr.read()
        stderr.close()
    return out if not xpath_expr else xpath(out, xpath_expr)