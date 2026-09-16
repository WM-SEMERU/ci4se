def has_shell_command(self, command):
    try:
        output = self.shell(['command', '-v', command]).decode('utf-8').strip()
        return command in output
    except AdbError:
        return False