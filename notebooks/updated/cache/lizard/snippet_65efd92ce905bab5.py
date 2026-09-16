def run(self, bin, *args, **kwargs):
    bin = self._bin(bin)
    cmd = [bin] + list(args)
    shell = kwargs.get('shell', False)
    call = kwargs.pop('call', False)
    input_ = kwargs.pop('input_', None)
    if shell:
        cmd = list_to_shell_command(cmd)
    try:
        if self._is_windows:
            kwargs['shell'] = True
        if input_:
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=
                subprocess.PIPE, stderr=subprocess.STDOUT, **kwargs)
            output = p.communicate(encode(input_))[0]
        elif call:
            return subprocess.call(cmd, stderr=subprocess.STDOUT, **kwargs)
        else:
            output = subprocess.check_output(cmd, stderr=subprocess.STDOUT,
                **kwargs)
    except CalledProcessError as e:
        raise EnvCommandError(e)
    return decode(output)