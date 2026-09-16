def _set_virtualbox(self):
    from os import environ
    if not environ.get('DOCKER_CERT_PATH'):
        import re
        sys_command = 'docker-machine env %s' % self.vbox
        cmd_output = self.command(sys_command)
        variable_list = ['DOCKER_TLS_VERIFY', 'DOCKER_HOST',
            'DOCKER_CERT_PATH', 'DOCKER_MACHINE_NAME']
        for variable in variable_list:
            env_start = '%s="' % variable
            env_end = '"\\n'
            env_regex = '%s.*?%s' % (env_start, env_end)
            env_pattern = re.compile(env_regex)
            env_statement = env_pattern.findall(cmd_output)
            env_var = env_statement[0].replace(env_start, '').replace('"\n', ''
                )
            environ[variable] = env_var
    return True