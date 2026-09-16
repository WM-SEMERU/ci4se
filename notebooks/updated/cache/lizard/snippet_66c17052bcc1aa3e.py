def command_output(self, command, shell=False, capture_stderr=False,
    localized=False):
    if isinstance(command, basestring):
        pretty_cmd = command
    else:
        pretty_cmd = ' '.join(command)
    if not shell and isinstance(command, basestring):
        command = shlex.split(command)
    stderr = STDOUT if capture_stderr else PIPE
    env = self._english_env if not localized else None
    try:
        process = Popen(command, stdout=PIPE, stderr=stderr, close_fds=True,
            universal_newlines=True, shell=shell, env=env)
    except Exception as e:
        msg = 'Command `{cmd}` {error}'.format(cmd=pretty_cmd, error=e)
        raise exceptions.CommandError(msg, error_code=e.errno)
    output, error = process.communicate()
    if self._is_python_2 and isinstance(output, str):
        output = output.decode('utf-8')
        error = error.decode('utf-8')
    retcode = process.poll()
    if retcode:
        if retcode == -15:
            msg = 'Command `{cmd}` returned SIGTERM (ignoring)'
            self.log(msg.format(cmd=pretty_cmd))
        else:
            msg = 'Command `{cmd}` returned non-zero exit status {error}'
            output_oneline = output.replace('\n', ' ')
            if output_oneline:
                msg += ' ({output})'
            msg = msg.format(cmd=pretty_cmd, error=retcode, output=
                output_oneline)
            raise exceptions.CommandError(msg, error_code=retcode, error=
                error, output=output)
    return output