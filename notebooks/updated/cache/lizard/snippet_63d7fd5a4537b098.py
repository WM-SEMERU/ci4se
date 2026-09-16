def _encrypt(self, archive):
    arc_name = archive.replace('sosreport-', 'secured-sosreport-')
    arc_name += '.gpg'
    enc_cmd = 'gpg --batch -o %s ' % arc_name
    env = None
    if self.enc_opts['key']:
        enc_cmd += '--trust-model always -e -r %s ' % self.enc_opts['key']
        enc_cmd += archive
    if self.enc_opts['password']:
        passwd = '%s' % self.enc_opts['password'].replace('\'"', '')
        env = {'sos_gpg': passwd}
        enc_cmd += '-c --passphrase-fd 0 '
        enc_cmd = '/bin/bash -c "echo $sos_gpg | %s"' % enc_cmd
        enc_cmd += archive
    r = sos_get_command_output(enc_cmd, timeout=0, env=env)
    if r['status'] == 0:
        return arc_name
    elif r['status'] == 2:
        if self.enc_opts['key']:
            msg = 'Specified key not in keyring'
        else:
            msg = 'Could not read passphrase'
    else:
        msg = 'gpg exited with code %s' % r['status']
    raise Exception(msg)