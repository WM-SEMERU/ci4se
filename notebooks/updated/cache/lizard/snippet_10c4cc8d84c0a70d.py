def handle_event(self, package):
    if not self.ready:
        raise tornado.gen.Return()
    tag, data = salt.utils.event.SaltEvent.unpack(package)
    log.debug("Minion of '%s' is handling event tag '%s'", self.opts[
        'master'], tag)
    tag_functions = {'beacons_refresh': self._handle_tag_beacons_refresh,
        'environ_setenv': self._handle_tag_environ_setenv, 'fire_master':
        self._handle_tag_fire_master, 'grains_refresh': self.
        _handle_tag_grains_refresh, 'matchers_refresh': self.
        _handle_tag_matchers_refresh, 'manage_schedule': self.
        _handle_tag_manage_schedule, 'manage_beacons': self.
        _handle_tag_manage_beacons, '_minion_mine': self.
        _handle_tag_minion_mine, 'module_refresh': self.
        _handle_tag_module_refresh, 'pillar_refresh': self.
        _handle_tag_pillar_refresh, 'salt/auth/creds': self.
        _handle_tag_salt_auth_creds, '_salt_error': self.
        _handle_tag_salt_error, '__schedule_return': self.
        _handle_tag_schedule_return, master_event(type='disconnected'):
        self._handle_tag_master_disconnected_failback, master_event(type=
        'failback'): self._handle_tag_master_disconnected_failback,
        master_event(type='connected'): self._handle_tag_master_connected}
    for tag_function in tag_functions:
        if tag.startswith(tag_function):
            tag_functions[tag_function](tag, data)