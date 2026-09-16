def state(self, container_id=None, sudo=None, sync_socket=None):
    sudo = self._get_sudo(sudo)
    container_id = self.get_container_id(container_id)
    cmd = self._init_command('state')
    if sync_socket != None:
        cmd = cmd + ['--sync-socket', sync_socket]
    cmd.append(container_id)
    result = self._run_command(cmd, sudo=sudo, quiet=True)
    if result != None:
        if isinstance(result, str):
            return json.loads(result)