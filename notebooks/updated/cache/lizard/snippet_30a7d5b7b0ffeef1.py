def multisend(self, send, send_dict, expect=None, shutit_pexpect_child=None,
    timeout=shutit_global.shutit_global_object.default_timeout, check_exit=
    None, fail_on_empty_before=True, record_command=True, exit_values=None,
    escape=False, echo=None, note=None, secret=False, nonewline=False,
    loglevel=logging.DEBUG):
    shutit_global.shutit_global_object.yield_to_draw()
    assert isinstance(send_dict, dict), shutit_util.print_debug()
    shutit_pexpect_child = (shutit_pexpect_child or self.
        get_current_shutit_pexpect_session().pexpect_child)
    expect = expect or self.get_current_shutit_pexpect_session().default_expect
    shutit_pexpect_session = self.get_shutit_pexpect_session_from_child(
        shutit_pexpect_child)
    return shutit_pexpect_session.multisend(ShutItSendSpec(
        shutit_pexpect_session, send=send, send_dict=send_dict, expect=
        expect, timeout=timeout, check_exit=check_exit,
        fail_on_empty_before=fail_on_empty_before, record_command=
        record_command, exit_values=exit_values, escape=escape, echo=echo,
        note=note, loglevel=loglevel, secret=secret, nonewline=nonewline))