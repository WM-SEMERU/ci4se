def format_installed_dap_list(simple=False):
    lines = []
    if simple:
        for pkg in sorted(get_installed_daps()):
            lines.append(pkg)
    else:
        for pkg, instances in sorted(get_installed_daps_detailed().items()):
            versions = []
            for instance in instances:
                location = utils.unexpanduser(instance['location'])
                version = instance['version']
                if not versions:
                    version = utils.bold(version)
                versions.append('{v}:{p}'.format(v=version, p=location))
            pkg = utils.bold(pkg)
            lines.append('{pkg} ({versions})'.format(pkg=pkg, versions=' '.
                join(versions)))
    return lines