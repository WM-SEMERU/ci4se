def get_default_config(self):
    config = super(NtpdCollector, self).get_default_config()
    config.update({'path': 'ntpd', 'ntpq_bin': self.find_binary(
        '/usr/bin/ntpq'), 'ntpdc_bin': self.find_binary('/usr/bin/ntpdc'),
        'use_sudo': False, 'sudo_cmd': self.find_binary('/usr/bin/sudo')})
    return config