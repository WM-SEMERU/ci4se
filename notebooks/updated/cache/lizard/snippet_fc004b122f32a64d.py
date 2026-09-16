def getHostOffset(self, host):
    info_dict = {}
    output = util.exec_command([ntpdateCmd, '-u', '-q', host])
    for line in output.splitlines():
        mobj = re.match(
            'server.*,\\s*stratum\\s+(\\d),.*offset\\s+([\\d\\.-]+),.*delay\\s+([\\d\\.]+)\\s*$'
            , line)
        if mobj:
            info_dict['stratum'] = int(mobj.group(1))
            info_dict['delay'] = float(mobj.group(3))
            info_dict['offset'] = float(mobj.group(2))
            return info_dict
    return info_dict