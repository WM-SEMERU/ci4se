def _state_command(self, container_id=None, command='start', sudo=None):
    sudo = self._get_sudo(sudo)
    container_id = self.get_container_id(container_id)
    cmd = self._init_command(command)
    cmd.append(container_id)
    return self._run_and_return(cmd, sudo)