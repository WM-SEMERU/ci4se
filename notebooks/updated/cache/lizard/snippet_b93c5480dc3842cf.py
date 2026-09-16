def check_file_exists(self, remote_cmd=''):
    if self.direction == 'put':
        if not remote_cmd:
            remote_cmd = 'dir {}{}'.format(self.file_system, self.dest_file)
        remote_out = self.ssh_ctl_chan.send_command_expect(remote_cmd)
        search_string = '{}.*Usage for'.format(self.dest_file)
        if 'No such file or directory' in remote_out:
            return False
        elif re.search(search_string, remote_out, flags=re.DOTALL):
            return True
        else:
            raise ValueError('Unexpected output from check_file_exists')
    elif self.direction == 'get':
        return os.path.exists(self.dest_file)