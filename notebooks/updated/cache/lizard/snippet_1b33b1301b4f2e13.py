def execute(self, image=None, command=None, app=None, writable=False,
    contain=False, bind=None, stream=False, nv=False, return_result=False):
    from spython.utils import check_install
    check_install()
    cmd = self._init_command('exec')
    if nv is True:
        cmd += ['--nv']
    if isinstance(image, list):
        command = image
        image = None
    if command is not None:
        if image is None:
            image = self._get_uri()
            self.quiet = True
        if isinstance(image, self.instance):
            image = image.get_uri()
        if bind is not None:
            cmd += self._generate_bind_list(bind)
        if app is not None:
            cmd = cmd + ['--app', app]
        sudo = False
        if writable is True:
            sudo = True
        if not isinstance(command, list):
            command = command.split(' ')
        cmd = cmd + [image] + command
        if stream is False:
            return self._run_command(cmd, sudo=sudo, return_result=
                return_result)
        return stream_command(cmd, sudo=sudo)
    bot.error('Please include a command (list) to execute.')