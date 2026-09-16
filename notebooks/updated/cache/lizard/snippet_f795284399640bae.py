def _bse_cli_get_info(args):
    bs_meta = api.get_metadata(args.data_dir)[args.basis]
    ret = []
    ret.append('-' * 80)
    ret.append(args.basis)
    ret.append('-' * 80)
    ret.append('    Display Name: ' + bs_meta['display_name'])
    ret.append('     Description: ' + bs_meta['description'])
    ret.append('            Role: ' + bs_meta['role'])
    ret.append('          Family: ' + bs_meta['family'])
    ret.append('  Function Types: ' + ','.join(bs_meta['functiontypes']))
    ret.append('  Latest Version: ' + bs_meta['latest_version'])
    ret.append('')
    aux = bs_meta['auxiliaries']
    if len(aux) == 0:
        ret.append('Auxiliary Basis Sets: None')
    else:
        ret.append('Auxiliary Basis Sets:')
        ret.extend(format_columns(list(aux.items()), '    '))
    ver = bs_meta['versions']
    ret.append('')
    ret.append('Versions:')
    version_lines = format_columns([(k, compact_elements(v['elements']), v[
        'revdesc']) for k, v in ver.items()], '    ')
    ret.extend(version_lines)
    return '\n'.join(ret)