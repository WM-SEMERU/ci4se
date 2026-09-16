def login(self, command='su -', user=None, password=None, prompt_prefix=
    None, expect=None, timeout=shutit_global.shutit_global_object.
    default_timeout, escape=False, echo=None, note=None, go_home=True,
    fail_on_fail=True, is_ssh=True, check_sudo=True, loglevel=logging.DEBUG):
    shutit_global.shutit_global_object.yield_to_draw()
    shutit_pexpect_session = self.get_current_shutit_pexpect_session()
    return shutit_pexpect_session.login(ShutItSendSpec(
        shutit_pexpect_session, user=user, send=command, password=password,
        prompt_prefix=prompt_prefix, expect=expect, timeout=timeout, escape
        =escape, echo=echo, note=note, go_home=go_home, fail_on_fail=
        fail_on_fail, is_ssh=is_ssh, check_sudo=check_sudo, loglevel=loglevel))