def run_openstack_sg_cmds(self, commands, switch):
    if not switch:
        LOG.exception('No client found for switch')
        return []
    if len(commands) == 0:
        return []
    command_start = ['enable', 'configure']
    command_end = ['exit']
    full_command = command_start + commands + command_end
    return self._run_eos_cmds(full_command, switch)