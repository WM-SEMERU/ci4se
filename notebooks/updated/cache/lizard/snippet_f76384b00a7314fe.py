def _getImports_ldd(pth):
    rslt = set()
    if is_aix:
        lddPattern = re.compile('\\s+(.*?)(\\(.*\\))')
    else:
        lddPattern = re.compile('\\s+(.*?)\\s+=>\\s+(.*?)\\s+\\(.*\\)')
    for line in compat.exec_command('ldd', pth).strip().splitlines():
        m = lddPattern.search(line)
        if m:
            if is_aix:
                lib = m.group(1)
                name = os.path.basename(lib) + m.group(2)
            else:
                name, lib = m.group(1), m.group(2)
            if name[:10] in ('linux-gate', 'linux-vdso'):
                continue
            if os.path.exists(lib):
                if lib not in rslt:
                    rslt.add(lib)
            else:
                logger.error('Can not find %s in path %s (needed by %s)',
                    name, lib, pth)
    return rslt