def _check_file_exists_unix(self, remote_cmd=''):
    if self.direction == 'put':
        self.ssh_ctl_chan._enter_shell()
        remote_cmd = 'ls {}'.format(self.file_system)
        remote_out = self.ssh_ctl_chan.send_command(remote_cmd,
            expect_string='[\\$#]')
        self.ssh_ctl_chan._return_cli()
        return self.dest_file in remote_out
    elif self.direction == 'get':
        return os.path.exists(self.dest_file)