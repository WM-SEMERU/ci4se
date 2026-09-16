def cid(i):
    o = i.get('out', '')
    ruoa = i.get('repo_uoa', '')
    muoa = i.get('module_uoa', '')
    duoa = i.get('data_uoa', '')
    if ruoa == '' and muoa == '' and duoa == '':
        r = detect_cid_in_current_path(i)
    else:
        r = find({'repo_uoa': ruoa, 'module_uoa': muoa, 'data_uoa': duoa})
    if r['return'] > 0:
        return r
    rx = convert_entry_to_cid(r)
    if rx['return'] > 0:
        return rx
    cid = rx['cid']
    if o == 'con':
        out(cid)
        rx = copy_to_clipboard({'string': cid})
    return r