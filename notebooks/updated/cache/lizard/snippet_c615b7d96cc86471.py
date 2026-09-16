def push_external_commands_to_schedulers(self):
    for external_command in self.external_commands:
        self.external_commands_manager.resolve_command(external_command)
    sent = False
    for scheduler_link in self.conf.schedulers:
        ext_cmds = scheduler_link.external_commands
        if ext_cmds and scheduler_link.reachable:
            logger.debug('Sending %d commands to the scheduler %s', len(
                ext_cmds), scheduler_link.name)
            if scheduler_link.push_external_commands(ext_cmds):
                statsmgr.counter('external-commands.pushed.count', len(
                    ext_cmds))
                sent = True
        if sent:
            scheduler_link.external_commands.clear()