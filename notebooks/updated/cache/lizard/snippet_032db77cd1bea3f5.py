def send_host_file(self, path, hostfilepath, expect=None,
    shutit_pexpect_child=None, note=None, user=None, group=None, loglevel=
    logging.INFO):
    shutit_global.shutit_global_object.yield_to_draw()
    shutit_pexpect_child = (shutit_pexpect_child or self.
        get_current_shutit_pexpect_session().pexpect_child)
    expect = expect or self.get_current_shutit_pexpect_session().default_expect
    shutit_pexpect_session = self.get_shutit_pexpect_session_from_child(
        shutit_pexpect_child)
    self.handle_note(note, 'Sending file from host: ' + hostfilepath +
        ' to target path: ' + path)
    self.log('Sending file from host: ' + hostfilepath + ' to: ' + path,
        level=loglevel)
    if user is None:
        user = shutit_pexpect_session.whoami()
    if group is None:
        group = self.whoarewe()
    if os.path.isfile(hostfilepath):
        shutit_pexpect_session.send_file(path, codecs.open(hostfilepath,
            mode='rb', encoding='iso-8859-1').read(), user=user, group=
            group, loglevel=loglevel, encoding='iso-8859-1')
    elif os.path.isdir(hostfilepath):
        self.send_host_dir(path, hostfilepath, user=user, group=group,
            loglevel=loglevel)
    else:
        self.fail('send_host_file - file: ' + hostfilepath +
            ' does not exist as file or dir. cwd is: ' + os.getcwd(),
            shutit_pexpect_child=shutit_pexpect_child, throw_exception=False)
    self.handle_note_after(note=note)
    return True