def setup(self):
    conf_file = self.get_option('conf_file')
    log_dir = '/var/log/watchdog'
    self.add_copy_spec([conf_file, '/etc/sysconfig/watchdog'])
    self.add_copy_spec(['/etc/watchdog.d', '/usr/libexec/watchdog/scripts'])
    try:
        res = self.get_log_dir(conf_file)
        if res:
            log_dir = res
    except IOError as ex:
        self._log_warn('Could not read %s: %s' % (conf_file, ex))
    if self.get_option('all_logs'):
        log_files = glob(os.path.join(log_dir, '*'))
    else:
        log_files = glob(os.path.join(log_dir, '*.stdout')) + glob(os.path.
            join(log_dir, '*.stderr'))
    self.add_copy_spec(log_files)
    for dev in glob('/dev/watchdog*'):
        self.add_cmd_output('wdctl %s' % dev)