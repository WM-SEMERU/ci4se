def list_upgrades(jid, style='group', outputter='nested', ext_source=None):
    mminion = salt.minion.MasterMinion(__opts__)
    returner = _get_returner((__opts__['ext_job_cache'], ext_source,
        __opts__['master_job_cache']))
    data = mminion.returners['{0}.get_jid'.format(returner)](jid)
    pkgs = {}
    if style == 'group':
        for minion in data:
            results = data[minion]['return']
            for pkg, pkgver in six.iteritems(results):
                if pkg not in six.iterkeys(pkgs):
                    pkgs[pkg] = {pkgver: {'hosts': []}}
                if pkgver not in six.iterkeys(pkgs[pkg]):
                    pkgs[pkg].update({pkgver: {'hosts': []}})
                pkgs[pkg][pkgver]['hosts'].append(minion)
    if outputter:
        salt.output.display_output(pkgs, outputter, opts=__opts__)
    return pkgs