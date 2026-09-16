def parse_dist(self, os_version):
    supported = {'rhel': ['rhel', 'redhat', 'red hat'], 'sles': ['suse',
        'sles'], 'ubuntu': ['ubuntu']}
    os_version = os_version.lower()
    for distro, patterns in supported.items():
        for i in patterns:
            if os_version.startswith(i):
                remain = os_version.split(i, 2)[1]
                release = self._parse_release(os_version, distro, remain)
                return distro, release
    msg = 'Can not handle os: %s' % os_version
    raise exception.ZVMException(msg=msg)