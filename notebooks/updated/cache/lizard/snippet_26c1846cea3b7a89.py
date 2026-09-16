def setup_aa_profile(self):
    self()
    if not self.ctxt:
        log('Not enabling apparmor Profile')
        return
    self.install_aa_utils()
    cmd = ['aa-{}'.format(self.ctxt['aa_profile_mode'])]
    cmd.append(self.ctxt['aa_profile'])
    log('Setting up the apparmor profile for {} in {} mode.'.format(self.
        ctxt['aa_profile'], self.ctxt['aa_profile_mode']))
    try:
        check_call(cmd)
    except CalledProcessError as e:
        if self.ctxt['aa_profile_mode'] == 'disable':
            log('Manually disabling the apparmor profile for {}.'.format(
                self.ctxt['aa_profile']))
            self.manually_disable_aa_profile()
            return
        status_set('blocked', 'Apparmor profile {} failed to be set to {}.'
            .format(self.ctxt['aa_profile'], self.ctxt['aa_profile_mode']))
        raise e