def _bsecurate_cli_component_file_refs(args):
    data = curate.component_file_refs(args.files)
    s = ''
    for cfile, cdata in data.items():
        s += cfile + '\n'
        rows = []
        for el, refs in cdata:
            rows.append(('    ' + el, ' '.join(refs)))
        s += '\n'.join(format_columns(rows)) + '\n\n'
    return s