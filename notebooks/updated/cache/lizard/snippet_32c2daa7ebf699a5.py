def pkg_checksum(binary, repo):
    md5 = 'None'
    if repo == 'slack_patches' and _meta_.slack_rel == 'stable':
        CHECKSUMS_md5 = URL(mirrors('CHECKSUMS.md5', 'patches/')).reading()
    elif repo == 'slack_patches' and _meta_.slack_rel == 'current':
        CHECKSUMS_md5 = URL(mirrors('CHECKSUMS.md5', '')).reading()
    elif repo == 'slpkg':
        CHECKSUMS_md5 = URL(_meta_.CHECKSUMS_link).reading()
    else:
        lib = '{0}{1}_repo/CHECKSUMS.md5'.format(_meta_.lib_path, repo)
        f = open(lib, 'r')
        CHECKSUMS_md5 = f.read()
        f.close()
    for line in CHECKSUMS_md5.splitlines():
        if line.endswith('/{0}'.format(binary)):
            md5 = line.split()[0]
    return md5