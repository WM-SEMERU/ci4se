def ps(self):
    sys_command = 'docker ps -a'
    sys_output = self.command(sys_command)
    container_list = self._ps(sys_output)
    return container_list