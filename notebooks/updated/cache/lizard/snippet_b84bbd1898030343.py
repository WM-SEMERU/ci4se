def compare_config(self):
    if self.config_session is None:
        return ''
    else:
        commands = ['show session-config named %s diffs' % self.config_session]
        result = self.device.run_commands(commands, encoding='text')[0][
            'output']
        result = '\n'.join(result.splitlines()[2:])
        return result.strip()