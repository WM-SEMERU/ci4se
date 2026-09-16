def _build_amps_list(self, amp_value, processlist):
    ret = []
    try:
        for p in processlist:
            add_it = False
            if re.search(amp_value.regex(), p['name']) is not None:
                add_it = True
            else:
                for c in p['cmdline']:
                    if re.search(amp_value.regex(), c) is not None:
                        add_it = True
                        break
            if add_it:
                ret.append({'pid': p['pid'], 'cpu_percent': p['cpu_percent'
                    ], 'memory_percent': p['memory_percent']})
    except (TypeError, KeyError) as e:
        logger.debug('Can not build AMPS list ({})'.format(e))
    return ret