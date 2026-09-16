def do_finalize(self):
    shutit_global.shutit_global_object.yield_to_draw()

    def _finalize(self):
        self.stop_all()
        self.log('PHASE: finalizing object ' + str(self), level=logging.DEBUG)
        for module_id in self.module_ids(rev=True):
            if self.is_installed(self.shutit_map[module_id]):
                self.login(prompt_prefix=module_id, command=shutit_global.
                    shutit_global_object.bash_startup_command, echo=False)
                if not self.shutit_map[module_id].finalize(self):
                    self.fail(module_id + ' failed on finalize',
                        shutit_pexpect_child=self.
                        get_shutit_pexpect_session_from_id('target_child').
                        pexpect_child)
                self.logout(echo=False)
    _finalize(self)