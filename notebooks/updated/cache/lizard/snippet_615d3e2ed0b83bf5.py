def get_shutit_pexpect_session_from_child(self, shutit_pexpect_child):
    shutit_global.shutit_global_object.yield_to_draw()
    if not isinstance(shutit_pexpect_child, pexpect.pty_spawn.spawn):
        self.fail('Wrong type in get_shutit_pexpect_session_child: ' + str(
            type(shutit_pexpect_child)), throw_exception=True)
    for key in self.shutit_pexpect_sessions:
        if self.shutit_pexpect_sessions[key
            ].pexpect_child == shutit_pexpect_child:
            return self.shutit_pexpect_sessions[key]
    return self.fail('Should not get here in get_shutit_pexpect_session',
        throw_exception=True)