def _exec_command(self, command: str):
    stdin, stdout, stderr = self._ssh.exec_command(command)
    stdout.read()
    stderr.read()
    stdin.close()