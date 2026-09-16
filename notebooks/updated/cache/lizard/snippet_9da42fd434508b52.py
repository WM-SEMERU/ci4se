def check_instance(function):

    def wrapper(self, *args, **kwargs):
        func_trans = {'commit': manager.Manager, 'compare_config': manager.
            Manager, 'commit_check': manager.Manager, 'device_info':
            manager.Manager, 'diff_config': manager.Manager, 'health_check':
            manager.Manager, 'interface_errors': manager.Manager, 'op_cmd':
            paramiko.client.SSHClient, 'shell_cmd': paramiko.client.
            SSHClient, 'scp_pull': paramiko.client.SSHClient, 'scp_push':
            paramiko.client.SSHClient}
        if self.username == 'root' and function.__name__ == 'op_cmd':
            if not self._session:
                self.conn_type = 'paramiko'
                self.connect()
            if not self._shell:
                self.conn_type = 'root'
                self.connect()
            self.shell_to_cli()
        elif function.__name__ == 'shell_cmd':
            if not self._shell:
                self.conn_type = 'shell'
                self.connect()
            self.cli_to_shell()
        if isinstance(self._session, func_trans[function.__name__]):
            if function.__name__ in ['scp_pull', 'scp_push']:
                if not isinstance(self._scp, SCPClient):
                    self.conn_type = 'scp'
                    self.connect()
        else:
            self.disconnect()
            if function.__name__ == 'op_cmd':
                self.conn_type = 'paramiko'
            elif function.__name__ in ['scp_pull', 'scp_push']:
                self.conn_type = 'scp'
            else:
                self.conn_type = 'ncclient'
            self.connect()
        return function(self, *args, **kwargs)
    return wrapper