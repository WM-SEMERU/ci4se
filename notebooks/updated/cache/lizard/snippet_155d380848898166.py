def run(self, timeout=10 * 60):
    cmd = 'install all nxos {dir}:{bin}'.format(dir=self.DESTDIR, bin=self.
        image)
    self.device.api.exec_opcmd('terminal dont-ask', msg_type=
        'cli_show_ascii', timeout=timeout)
    run = self.device.api.exec_opcmd
    run(cmd, msg_type='cli_show_ascii', timeout=timeout)