def _active_mounts_aix(ret):
    for line in __salt__['cmd.run_stdout']('mount -p').split('\n'):
        comps = re.sub('\\s+', ' ', line).split()
        if comps:
            if comps[0] == 'node' or comps[0] == '--------':
                continue
            comps_len = len(comps)
            if line.startswith((' ', '\t')):
                curr_opts = _resolve_user_group_names(comps[6].split(',')
                    ) if 7 == comps_len else []
                if curr_opts:
                    ret[comps[1]] = {'device': comps[0], 'fstype': comps[2],
                        'opts': curr_opts}
                else:
                    ret[comps[1]] = {'device': comps[0], 'fstype': comps[2]}
            else:
                curr_opts = _resolve_user_group_names(comps[7].split(',')
                    ) if 8 == comps_len else []
                if curr_opts:
                    ret[comps[2]] = {'node': comps[0], 'device': comps[1],
                        'fstype': comps[3], 'opts': curr_opts}
                else:
                    ret[comps[2]] = {'node': comps[0], 'device': comps[1],
                        'fstype': comps[3]}
    return ret