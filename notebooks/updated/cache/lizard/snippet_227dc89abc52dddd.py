def complete_vrf_virtual(arg):
    ret = complete_vrf(arg)
    search_string = ''
    if arg is not None:
        search_string = '^%s' % arg
    if re.match(search_string, 'all'):
        ret.append('all')
    return ret