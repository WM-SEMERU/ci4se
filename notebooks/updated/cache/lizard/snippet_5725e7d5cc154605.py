def lsb_release(self, loglevel=logging.DEBUG):
    shutit = self.shutit
    d = {}
    self.send(ShutItSendSpec(self, send=' command lsb_release -a',
        check_exit=False, echo=False, loglevel=loglevel, ignore_background=
        True))
    res = shutit.match_string(self.pexpect_child.before,
        '^Distributor[\\s]*ID:[\\s]*(.*)$')
    if isinstance(res, str):
        dist_string = res
        d['distro'] = dist_string.lower().strip()
        try:
            d['install_type'] = package_map.INSTALL_TYPE_MAP[dist_string.
                lower()]
        except KeyError:
            raise Exception("Distribution '%s' is not supported." % dist_string
                )
    else:
        return d
    res = shutit.match_string(self.pexpect_child.before, '^Release:[\\s*](.*)$'
        )
    if isinstance(res, str):
        version_string = res
        d['distro_version'] = version_string
    return d