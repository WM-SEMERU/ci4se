def _get_changed_cfg_pkgs(self, data):
    f_data = dict()
    for pkg_name, pkg_files in data.items():
        cfgs = list()
        cfg_data = list()
        if self.grains_core.os_data().get('os_family') == 'Debian':
            cfg_data = salt.utils.stringutils.to_str(self._syscall('dpkg',
                None, None, '--verify', pkg_name)[0]).split(os.linesep)
        elif self.grains_core.os_data().get('os_family') in ['Suse', 'redhat']:
            cfg_data = salt.utils.stringutils.to_str(self._syscall('rpm',
                None, None, '-V', '--nodeps', '--nodigest', '--nosignature',
                '--nomtime', '--nolinkto', pkg_name)[0]).split(os.linesep)
        for line in cfg_data:
            line = line.strip()
            if not line or line.find(' c ') < 0 or line.split(' ')[0].find('5'
                ) < 0:
                continue
            cfg_file = line.split(' ')[-1]
            if cfg_file in pkg_files:
                cfgs.append(cfg_file)
        if cfgs:
            f_data[pkg_name] = cfgs
    return f_data