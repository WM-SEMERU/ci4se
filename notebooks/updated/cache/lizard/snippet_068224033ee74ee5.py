def getStats(self):
    info_dict = {}
    args = [varnishstatCmd, '-1']
    if self._instance is not None:
        args.extend(['-n', self._instance])
    output = util.exec_command(args)
    if self._descDict is None:
        self._descDict = {}
    for line in output.splitlines():
        mobj = re.match(
            '(\\S+)\\s+(\\d+)\\s+(\\d+\\.\\d+|\\.)\\s+(\\S.*\\S)\\s*$', line)
        if mobj:
            fname = mobj.group(1).replace('.', '_')
            info_dict[fname] = util.parse_value(mobj.group(2))
            self._descDict[fname] = mobj.group(4)
    return info_dict