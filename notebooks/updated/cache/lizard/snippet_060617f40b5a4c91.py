def _aix_get_machine_id():
    grains = {}
    cmd = salt.utils.path.which('lsattr')
    if cmd:
        data = __salt__['cmd.run']('{0} -El sys0'.format(cmd)) + os.linesep
        uuid_regexes = [re.compile('(?im)^\\s*os_uuid\\s+(\\S+)\\s+(.*)')]
        for regex in uuid_regexes:
            res = regex.search(data)
            if res and len(res.groups()) >= 1:
                grains['machine_id'] = res.group(1).strip()
                break
    else:
        log.error("The 'lsattr' binary was not found in $PATH.")
    return grains