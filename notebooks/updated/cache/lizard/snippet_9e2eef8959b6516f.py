def slack_package(prgnam):
    binaries, cache, binary = [], '0', ''
    for pkg in find_package(prgnam, _meta_.output):
        if pkg.startswith(prgnam) and pkg[:-4].endswith('_SBo'):
            binaries.append(pkg)
    for bins in binaries:
        if LooseVersion(bins) > LooseVersion(cache):
            binary = bins
            cache = binary
    if not binary:
        Msg().build_FAILED(prgnam)
        raise SystemExit(1)
    return [''.join(_meta_.output + binary)]