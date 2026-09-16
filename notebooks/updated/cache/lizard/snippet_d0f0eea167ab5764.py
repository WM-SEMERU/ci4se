def _check_output(self, command):
    try:
        if sys.version_info[0] > 2:
            return check_output(self.base_command + command, stderr=STDOUT
                ).decode('utf8')
        else:
            return check_output(self.base_command + command, stderr=STDOUT)
    except CalledProcessError as command_error:
        raise GitCommandException(*command_error.args)